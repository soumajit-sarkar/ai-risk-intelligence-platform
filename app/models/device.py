from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Device(Base):
    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )

    device_fingerprint: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    device_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    os: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    browser: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    is_trusted: Mapped[bool] = mapped_column(
        Boolean,
        server_default=text("false"),
        nullable=False,
    )

    first_seen_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    last_seen_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    user: Mapped["User | None"] = relationship(
        "User",
        back_populates="devices",
    )

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        back_populates="device",
    )
