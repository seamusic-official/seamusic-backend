"""sfdfds

Revision ID: 40e800f89180
Revises: 0bfccfc69ed2
Create Date: 2024-07-26 11:44:09.057230

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '40e800f89180'
down_revision: Union[str, None] = '0bfccfc69ed2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_views_beats_id', table_name='views')
    op.drop_index('ix_views_user_id', table_name='views')
    op.drop_table('views')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'views',
        sa.Column('beats_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('is_available', sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(['beats_id'], ['beats.id'], name='views_beats_id_fkey'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='views_user_id_fkey'),
        sa.PrimaryKeyConstraint('id', name='views_pkey')
    )
    op.create_index('ix_views_user_id', 'views', ['user_id'], unique=False)
    op.create_index('ix_views_beats_id', 'views', ['beats_id'], unique=False)
    # ### end Alembic commands ###
