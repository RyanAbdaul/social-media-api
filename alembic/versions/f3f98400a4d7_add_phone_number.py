"""add phone number

Revision ID: f3f98400a4d7
Revises: 3a5e738af818
Create Date: 2026-06-20 14:21:21.654093

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f3f98400a4d7'
down_revision: Union[str, Sequence[str], None] = '3a5e738af818'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=False))

def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    """Downgrade schema."""