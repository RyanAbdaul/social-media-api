"""Add created_at column to posts table

Revision ID: 6bbff84b9a95
Revises: ac7c48477392
Create Date: 2026-06-20 12:27:42.065636

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6bbff84b9a95'
down_revision: Union[str, Sequence[str], None] = 'ac7c48477392'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.rename_table('Posts', 'posts')
    op.add_column('posts', sa.Column(
        'created_at',
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.text('now()')
        ))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'created_at')
