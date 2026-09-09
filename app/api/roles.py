from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.authorization import require_role
from app.db.database import get_db
from app.models.role import Role
from app.models.user import User
from app.schemas.role import RoleResponse


router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@router.get(
    "",
    response_model=list[RoleResponse],
)
def get_roles(
    current_user: User = Depends(require_role("admin")),
    db: Session = Depends(get_db),
):
    """
    Return all non-deleted roles.

    Requires the authenticated user to have the admin role.
    """
    roles = db.scalars(
        select(Role).where(
            Role.is_deleted.is_(False),
        )
    ).all()

    return roles