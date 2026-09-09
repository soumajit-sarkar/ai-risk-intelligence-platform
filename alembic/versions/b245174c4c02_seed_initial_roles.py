"""seed initial roles

Revision ID: b245174c4c02

Revises: b47aec58e1da

Create Date: 2026-09-09 14:52:45.438531

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b245174c4c02"
down_revision: Union[str, Sequence[str], None] = "b47aec58e1da"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Seed initial system roles."""

    roles_table = sa.table(
        "roles",
        sa.column("name", sa.String(length=50)),
        sa.column("description", sa.Text),
        sa.column("is_deleted", sa.Boolean),
    )

    op.bulk_insert(
        roles_table,
        [
            {
                "name": "admin",
                "description": "Full administrative access.",
                "is_deleted": False,
            },
            {
                "name": "risk_analyst",
                "description": "Analyze and investigate risk.",
                "is_deleted": False,
            },
            {
                "name": "risk_viewer",
                "description": "Read-only access to risk information.",
                "is_deleted": False,
            },
        ],
    )


def downgrade() -> None:
    """Remove initial system roles."""

    roles_table = sa.table(
        "roles",
        sa.column("name", sa.String(length=50)),
    )

    op.execute(
        roles_table.delete().where(
            roles_table.c.name.in_(
                [
                    "admin",
                    "risk_analyst",
                    "risk_viewer",
                ]
            )
        )
    )