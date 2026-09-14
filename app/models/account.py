from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id", ondelete="RESTRICT"),
        nullable=False,
    )

    account_number: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
    )

    account_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    account_status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    opened_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    closed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
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

    customer: Mapped["Customer"] = relationship(
        "Customer",
        back_populates="accounts",
    )

    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction",
        back_populates="account",
    )
