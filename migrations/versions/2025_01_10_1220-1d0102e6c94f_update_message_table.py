"""Update message table

Revision ID: 1d0102e6c94f
Revises: 6eed0d93ce35
Create Date: 2025-01-10 12:20:49.579297

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d0102e6c94f'
down_revision: Union[str, None] = '6eed0d93ce35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('user_message', sa.Text(), nullable=False))
    op.drop_column('messages', 'question')
    op.drop_column('messages', 'answer')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('answer', sa.TEXT(), autoincrement=False, nullable=False))
    op.add_column('messages', sa.Column('question', sa.TEXT(), autoincrement=False, nullable=False))
    op.drop_column('messages', 'user_message')
    # ### end Alembic commands ###
