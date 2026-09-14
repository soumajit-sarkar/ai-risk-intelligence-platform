from datetime import datetime

from sqlalchemy import Boolean, Computed, DateTime, Index, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    active_email: Mapped[str | None] = mapped_column(
        String(255),
        Computed(
            "CASE WHEN is_deleted = 0 THEN email ELSE NULL END",
            persisted=True,
        ),
        nullable=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    password_hash: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    last_login_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        server_default=text("false"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    role_assignments: Mapped[list["UserRole"]] = relationship(
        "UserRole",
        foreign_keys="UserRole.user_id",
        back_populates="user",
    )

    role_assignments_made: Mapped[list["UserRole"]] = relationship(
        "UserRole",
        foreign_keys="UserRole.assigned_by",
        back_populates="assigned_by_user",
    )

    devices: Mapped[list["Device"]] = relationship(
        "Device",
        back_populates="user",
    )

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        back_populates="user",
    )

    __table_args__ = (
        Index(
            "ix_users_active_email",
            "active_email",
            unique=True,
        ),
    )