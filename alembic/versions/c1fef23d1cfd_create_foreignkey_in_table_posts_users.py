"""Create ForeignKey in table posts -> users)

Revision ID: c1fef23d1cfd
Revises: 643ef72fbae0
Create Date: 2026-06-20 13:50:02.206352

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1fef23d1cfd'
down_revision: Union[str, Sequence[str], None] = '643ef72fbae0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column(
        'user_id',
        sa.Integer(),
        nullable=False)
    )
    op.create_foreign_key(
                        'posts_users_fk',
                        source_table='posts',
                        referent_table='users',
                        local_cols=['user_id'],
                        remote_cols=['id'],
                        ondelete='CASCADE'
                        )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'user_id')