from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class UserRole(Base):
    __tablename__ = "user_roles"

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    role_id: Mapped[int] = mapped_column(
        ForeignKey(
            "roles.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    assigned_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    assigned_by: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        "User",
        foreign_keys=[user_id],
        back_populates="role_assignments",
    )

    role: Mapped["Role"] = relationship(
        "Role",
        foreign_keys=[role_id],
        back_populates="user_roles",
    )

    assigned_by_user: Mapped["User"] = relationship(
        "User",
        foreign_keys=[assigned_by],
        back_populates="role_assignments_made",
    )
