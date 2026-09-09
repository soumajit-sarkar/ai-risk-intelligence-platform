from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.api.authorization import require_role
from app.api.dependencies import get_current_user
from app.core.security import hash_password
from app.db.database import get_db
from app.models.role import Role
from app.models.user import User
from app.models.user_role import UserRole
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.schemas.user_role import UserRoleCreate, UserRoleResponse


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "",
    response_model=list[UserResponse],
)
def get_users(
    current_user: User = Depends(require_role("admin")),
    db: Session = Depends(get_db),
):
    """
    Return all non-deleted users.

    Requires the authenticated user to have the admin role.
    """
    users = db.scalars(
        select(User).where(
            User.is_deleted.is_(False),
        )
    ).all()

    return users


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_current_user_profile(
    current_user: User = Depends(get_current_user),
):
    """
    Return the currently authenticated user's profile.
    """
    return current_user


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new user.
    """
    existing_user = db.scalar(
        select(User).where(
            User.email == user_data.email,
            User.is_deleted.is_(False),
        )
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists.",
        )

    user = User(
        email=user_data.email,
        full_name=user_data.full_name,
        password_hash=hash_password(user_data.password),
        is_active=False,
        is_deleted=False,
    )

    db.add(user)

    try:
        db.commit()
        db.refresh(user)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists.",
        )

    return user


@router.put(
    "/{user_id}",
    response_model=UserResponse,
)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
):
    """
    Update a non-deleted user.
    """
    user = db.scalar(
        select(User).where(
            User.id == user_id,
            User.is_deleted.is_(False),
        )
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    existing_user = db.scalar(
        select(User).where(
            User.email == user_data.email,
            User.is_deleted.is_(False),
            User.id != user_id,
        )
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists.",
        )

    user.email = user_data.email
    user.full_name = user_data.full_name

    try:
        db.commit()
        db.refresh(user)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists.",
        )

    return user


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    """
    Soft-delete a user.
    """
    user = db.scalar(
        select(User).where(
            User.id == user_id,
            User.is_deleted.is_(False),
        )
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )

    user.is_deleted = True

    try:
        db.commit()

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Unable to delete user.",
        )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )


@router.post(
    "/{user_id}/roles",
    response_model=UserRoleResponse,
    status_code=status.HTTP_201_CREATED,
)
def assign_role_to_user(
    user_id: int,
    role_data: UserRoleCreate,
    current_user: User = Depends(require_role("admin")),
    db: Session = Depends(get_db),
):
    """
    Assign a role to a user.

    Requires the authenticated user to have the admin role.
    The authenticated admin is recorded as assigned_by.
    """

    target_user = db.scalar(
        select(User).where(
            User.id == user_id,
            User.is_deleted.is_(False),
        )
    )

    if target_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Target user not found.",
        )

    if not target_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Cannot assign a role to an inactive user.",
        )

    role = db.scalar(
        select(Role).where(
            Role.id == role_data.role_id,
            Role.is_deleted.is_(False),
        )
    )

    if role is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found.",
        )

    existing_assignment = db.scalar(
        select(UserRole).where(
            UserRole.user_id == user_id,
            UserRole.role_id == role_data.role_id,
        )
    )

    if existing_assignment is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This role is already assigned to the user.",
        )

    user_role = UserRole(
        user_id=user_id,
        role_id=role_data.role_id,
        assigned_by=current_user.id,
    )

    db.add(user_role)

    try:
        db.commit()
        db.refresh(user_role)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Unable to assign role to user.",
        )

    return user_role