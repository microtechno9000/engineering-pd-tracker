"""record table

Revision ID: a644232fe039
Revises: 844ad9855c6a
Create Date: 2023-07-06 13:12:12.077528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a644232fe039'
down_revision = '844ad9855c6a'
branch_labels = None
depends_on = '844ad9855c6a'


def upgrade() -> None:
    op.create_table(
        'record',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date_start', sa.Date),
        sa.Column('date_finish', sa.Date),
        sa.Column('date_expire', sa.Date),
        sa.Column('record_valid', sa.Boolean),
        sa.Column('title', sa.String(200)),
        sa.Column('description', sa.String(5000)),
        sa.Column('notes', sa.String(5000)),
        sa.Column('training_provider', sa.String(100)),
        sa.Column('training_location', sa.String(100)),
        sa.Column('duration', sa.Time),
        sa.Column('duration_risk', sa.Time),
        sa.Column('duration_business', sa.Time),
        sa.Column('duration_practice', sa.Time),
        sa.Column('training_activity_id', sa.Integer, nullable=True),
        sa.Column('training_type_id', sa.Integer, nullable=True),
        sa.Column('training_division_id', sa.String(500)),

        sa.ForeignKeyConstraint(['training_activity_id'], ['training_activity.id'], ),
        sa.ForeignKeyConstraint(['training_type_id'], ['training_type.id'], ),
        sa.ForeignKeyConstraint(['training_division_id'], ['training_division.id'], )
    )


def downgrade() -> None:
    op.drop_table('record')
