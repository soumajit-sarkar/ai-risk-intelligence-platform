"""make user email unique for active users

Revision ID: b47aec58e1da
Revises: 5a84c8f2208f
Create Date: 2026-09-08 11:24:42.974549

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b47aec58e1da"
down_revision: Union[str, Sequence[str], None] = "5a84c8f2208f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Remove the current unconditional unique constraint.
    op.drop_index(
        "ix_users_email",
        table_name="users",
    )

    # Store the email only for non-deleted users.
    op.add_column(
        "users",
        sa.Column(
            "active_email",
            sa.String(length=255),
            sa.Computed(
                "CASE WHEN is_deleted = 0 THEN email ELSE NULL END",
                persisted=True,
            ),
            nullable=True,
        ),
    )

    # Only active users participate in email uniqueness.
    op.create_index(
        "ix_users_active_email",
        "users",
        ["active_email"],
        unique=True,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        "ix_users_active_email",
        table_name="users",
    )

    op.drop_column(
        "users",
        "active_email",
    )

    # Restore the original unconditional email uniqueness.
    op.create_index(
        "ix_users_email",
        "users",
        ["email"],
        unique=True,
    )