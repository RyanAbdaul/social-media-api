"""add published column to posts

Revision ID: 4ac94cc676aa
Revises: c1fef23d1cfd
Create Date: 2026-06-20 14:02:26.440457

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ac94cc676aa'
down_revision: Union[str, Sequence[str], None] = 'c1fef23d1cfd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column(
        'published',
        sa.Boolean(),
        nullable=False,
        server_default='TRUE'
    ))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published')
