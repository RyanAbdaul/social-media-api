"""Add a phone number column to users table

Revision ID: 3a5e738af818
Revises: e54149cab92c
Create Date: 2026-06-20 14:17:30.456288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a5e738af818'
down_revision: Union[str, Sequence[str], None] = 'e54149cab92c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=False))

def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    """Downgrade schema."""
