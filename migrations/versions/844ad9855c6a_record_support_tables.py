"""record support tables

Revision ID: 844ad9855c6a
Revises: 
Create Date: 2023-07-06 12:50:15.780912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '844ad9855c6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'training_activity',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('activity', sa.String(100)),
        sa.Column('description', sa.String(500))
    )
    op.create_table(
        'training_type',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('type', sa.String(100)),
        sa.Column('description', sa.String(500)),
        sa.Column('conditions', sa.String(500))
    )


def downgrade() -> None:
    op.drop_table('training_activity')
    op.drop_table('training_type')
