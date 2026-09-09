from collections.abc import Callable

from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.db.database import get_db
from app.models.role import Role
from app.models.user import User
from app.models.user_role import UserRole


def require_role(*required_roles: str) -> Callable:
    """
    Require the authenticated user to have at least one
    of the specified roles.
    """

    if not required_roles:
        raise ValueError("At least one role is required.")

    def role_checker(
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db),
    ) -> User:
        user_role = db.scalar(
            select(Role.name)
            .join(
                UserRole,
                UserRole.role_id == Role.id,
            )
            .where(
                UserRole.user_id == current_user.id,
                Role.name.in_(required_roles),
                Role.is_deleted.is_(False),
            )
        )

        if user_role is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource.",
            )

        return current_user

    return role_checker