from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="RESTRICT"),
        nullable=False,
    )

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )

    transaction_ref: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    transaction_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    amount: Mapped[float] = mapped_column(
        Numeric(18, 2),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    transaction_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    merchant_name: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    merchant_category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    channel: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    location_country: Mapped[str | None] = mapped_column(
        String(2),
        nullable=True,
    )

    location_city: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    device_id: Mapped[int] = mapped_column(
        ForeignKey("devices.id", ondelete="RESTRICT"),
        nullable=False,
    )

    ip_address: Mapped[str | None] = mapped_column(
        String(45),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        server_default=text("'SUCCESS'"),
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

    is_deleted: Mapped[bool] = mapped_column(
        server_default=text("false"),
        nullable=False,
    )

    account: Mapped["Account"] = relationship(
        "Account",
        back_populates="transactions",
    )

    user: Mapped["User | None"] = relationship(
        "User",
        back_populates="transactions",
    )

    device: Mapped["Device"] = relationship(
        "Device",
        back_populates="transactions",
    )
