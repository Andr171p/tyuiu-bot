"""Bot message column

Revision ID: 82bb06766c12
Revises: 1d0102e6c94f
Create Date: 2025-01-10 12:25:05.546484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82bb06766c12'
down_revision: Union[str, None] = '1d0102e6c94f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('bot_message', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'bot_message')
    # ### end Alembic commands ###
