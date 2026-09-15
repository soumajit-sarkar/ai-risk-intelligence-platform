from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class TransactionCreate(BaseModel):
    account_id: int = Field(gt=0)
    transaction_ref: str = Field(min_length=1, max_length=50)
    transaction_type: str = Field(min_length=1, max_length=30)
    amount: Decimal = Field(gt=0, max_digits=18, decimal_places=2)
    currency: str = Field(min_length=1, max_length=10)
    transaction_time: datetime
    merchant_name: str | None = Field(default=None, max_length=150)
    merchant_category: str | None = Field(default=None, max_length=100)
    channel: str | None = Field(default=None, max_length=30)
    location_country: str | None = Field(default=None, min_length=2, max_length=2)
    location_city: str | None = Field(default=None, max_length=100)
    device_id: int = Field(gt=0)
    ip_address: str | None = Field(default=None, max_length=45)

class TransactionUpdate(BaseModel):
    transaction_type: str | None = Field(
        default=None,
        min_length=1,
        max_length=30,
    )
    amount: Decimal | None = Field(
        default=None,
        gt=0,
        max_digits=18,
        decimal_places=2,
    )
    currency: str | None = Field(
        default=None,
        min_length=1,
        max_length=10,
    )
    transaction_time: datetime | None = None
    merchant_name: str | None = Field(
        default=None,
        max_length=150,
    )
    merchant_category: str | None = Field(
        default=None,
        max_length=100,
    )
    channel: str | None = Field(
        default=None,
        max_length=30,
    )
    location_country: str | None = Field(
        default=None,
        min_length=2,
        max_length=2,
    )
    location_city: str | None = Field(
        default=None,
        max_length=100,
    )
    device_id: int | None = Field(
        default=None,
        gt=0,
    )
    ip_address: str | None = Field(
        default=None,
        max_length=45,
    )
    status: str | None = Field(
        default=None,
        min_length=1,
        max_length=20,
    )

class TransactionResponse(BaseModel):
    id: int
    account_id: int
    user_id: int | None
    transaction_ref: str
    transaction_type: str
    amount: Decimal
    currency: str
    transaction_time: datetime
    merchant_name: str | None
    merchant_category: str | None
    channel: str | None
    location_country: str | None
    location_city: str | None
    device_id: int
    ip_address: str | None
    status: str
    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    model_config = ConfigDict(
        from_attributes=True,
    )
