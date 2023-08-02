"""add data to tables

Revision ID: 39dbded117d1
Revises: a644232fe039
Create Date: 2023-07-28 12:31:25.665683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39dbded117d1'
down_revision = 'a644232fe039'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.bulk_insert(
        'training_activity',
        [
            {
                "id": 1,
                "activity": "Type I",
                "description": "Any tertiary courses taken either as an individual course or for a formal Post Graduate award.",
            },
        ]
    )

def downgrade() -> None:
    pass
