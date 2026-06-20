"""Create users table

Revision ID: 643ef72fbae0
Revises: 6bbff84b9a95
Create Date: 2026-06-20 13:44:22.879792

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '643ef72fbae0'
down_revision: Union[str, Sequence[str], None] = '6bbff84b9a95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users', 
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=False, server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
                )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')