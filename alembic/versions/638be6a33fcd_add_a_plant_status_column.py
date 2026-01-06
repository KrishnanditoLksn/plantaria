"""Add a plant status column

Revision ID: 638be6a33fcd
Revises: 80301d6ef78e
Create Date: 2026-01-06 23:22:59.455895

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '638be6a33fcd'
down_revision: Union[str, Sequence[str], None] = '80301d6ef78e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        op.alter_column(
            "plant",
            "race",
            new_column_name="status",
            existing_type=sa.String(length=255),
            nullable=True
        )
        pass



def downgrade() -> None:
    op.drop_index(op.f('ix_plant_age'), table_name='plant')
    op.drop_index(op.f('ix_plant_habitat'), table_name='plant')
    op.drop_index(op.f('ix_plant_id'), table_name='plant')
    op.drop_index(op.f('species'), table_name='plant')
    op.drop_table('plant')
    pass
