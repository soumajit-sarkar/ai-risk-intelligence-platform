from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.account import Account
from app.models.device import Device
from app.models.transaction import Transaction
from app.models.user import User
from app.schemas.transaction import TransactionCreate


def create_transaction(
    db: Session,
    transaction_data: TransactionCreate,
    current_user: User,
) -> Transaction:
    """
    Create a transaction for the authenticated user.
    """
    account = db.scalar(
        select(Account).where(
            Account.id == transaction_data.account_id
        )
    )

    if account is None:
        raise ValueError("Account not found.")

    device = db.scalar(
        select(Device).where(
            Device.id == transaction_data.device_id
        )
    )

    if device is None:
        raise ValueError("Device not found.")

    transaction = Transaction(
        account_id=transaction_data.account_id,
        user_id=current_user.id,
        transaction_ref=transaction_data.transaction_ref,
        transaction_type=transaction_data.transaction_type,
        amount=transaction_data.amount,
        currency=transaction_data.currency,
        transaction_time=transaction_data.transaction_time,
        merchant_name=transaction_data.merchant_name,
        merchant_category=transaction_data.merchant_category,
        channel=transaction_data.channel,
        location_country=transaction_data.location_country,
        location_city=transaction_data.location_city,
        device_id=transaction_data.device_id,
        ip_address=transaction_data.ip_address,
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction
