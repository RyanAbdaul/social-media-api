"""test

Revision ID: 28be4343506a
Revises: 
Create Date: 2026-06-22 11:39:37.730842

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28be4343506a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column('users', 'phone_number')


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')