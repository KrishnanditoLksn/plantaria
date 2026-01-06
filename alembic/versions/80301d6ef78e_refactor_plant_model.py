"""refactor plant model

Revision ID: 80301d6ef78e
Revises: 
Create Date: 2026-01-05 23:12:15.961228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '80301d6ef78e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def downgrade() -> None:
    op.drop_index(op.f('ix_plant_age'), table_name='plant')
    op.drop_index(op.f('ix_plant_habitat'), table_name='plant')
    op.drop_index(op.f('ix_plant_id'), table_name='plant')
    op.drop_index(op.f('species'), table_name='plant')
    op.drop_table('plant')


def upgrade() -> None:
    op.add_column(
        'plant',          
        sa.Column('race', sa.String(length=255), nullable=True),
    )
