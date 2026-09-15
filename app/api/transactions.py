from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.api.dependencies import get_db
from app.models.user import User
from app.schemas.transaction import TransactionCreate
from app.schemas.transaction import TransactionResponse, TransactionUpdate
from app.services.transaction_service import create_transaction, get_transactions, update_transaction


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


@router.post(
    "",
    response_model=TransactionResponse,
    status_code=201,
)
def create_transaction_endpoint(
    transaction_data: TransactionCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> TransactionResponse:
    """
    Create a new transaction for the authenticated user.
    """
    try:
        return create_transaction(
            db=db,
            transaction_data=transaction_data,
            current_user=current_user,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Transaction reference already exists.",
        )


@router.get(
    "",
    response_model=list[TransactionResponse],
)
def get_transactions_endpoint(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[TransactionResponse]:
    """
    Retrieve all active transactions belonging to the authenticated user.
    """
    return get_transactions(
        db=db,
        current_user=current_user,
    )

@router.patch(
    "/{transaction_id}",
    response_model=TransactionResponse,
)

def update_transaction_endpoint(
    transaction_id: int,
    transaction_data: TransactionUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> TransactionResponse:
    """
    Update an active transaction belonging to the authenticated user.
    """
    try:
        return update_transaction(
            db=db,
            transaction_id=transaction_id,
            transaction_data=transaction_data,
            current_user=current_user,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Unable to update transaction.",
        )