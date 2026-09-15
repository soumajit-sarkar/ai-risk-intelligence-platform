from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.account import Account
from app.models.device import Device
from app.models.transaction import Transaction
from app.models.user import User
from app.schemas.transaction import TransactionCreate, TransactionUpdate
from sqlalchemy.exc import IntegrityError

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

def get_transactions(
    db: Session,
    current_user: User,
) -> list[Transaction]:
    """
    Retrieve all active transactions belonging to the authenticated user.
    """
    transactions = db.scalars(
        select(Transaction).where(
            Transaction.user_id == current_user.id,
            Transaction.is_deleted.is_(False),
        )
    ).all()

    return transactions

def update_transaction(
    db: Session,
    transaction_id: int,
    transaction_data: TransactionUpdate,
    current_user: User,
) -> Transaction:
    """
    Update an active transaction belonging to the authenticated user.
    """
    transaction = db.scalar(
        select(Transaction).where(
            Transaction.id == transaction_id,
            Transaction.user_id == current_user.id,
            Transaction.is_deleted.is_(False),
        )
    )

    if transaction is None:
        raise ValueError("Transaction not found.")

    update_data = transaction_data.model_dump(
        exclude_unset=True,
    )

    if not update_data:
        return transaction

    if "device_id" in update_data:
        device = db.scalar(
            select(Device).where(
                Device.id == update_data["device_id"]
            )
        )

        if device is None:
            raise ValueError("Device not found.")

    for field, value in update_data.items():
        setattr(transaction, field, value)

    try:
        db.commit()
        db.refresh(transaction)

    except IntegrityError:
        db.rollback()
        raise

    return transaction


def delete_transaction(
    db: Session,
    transaction_id: int,
    current_user: User,
) -> Transaction:
    """
    Soft delete an active transaction belonging to the authenticated user.
    """
    transaction = db.scalar(
        select(Transaction).where(
            Transaction.id == transaction_id,
            Transaction.user_id == current_user.id,
            Transaction.is_deleted.is_(False),
        )
    )

    if transaction is None:
        raise ValueError("Transaction not found.")

    transaction.is_deleted = True

    try:
        db.commit()
        db.refresh(transaction)

    except IntegrityError:
        db.rollback()
        raise

    return transaction
