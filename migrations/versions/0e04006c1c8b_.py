"""empty message

Revision ID: 0e04006c1c8b
Revises: c84dd7a6c3ba
Create Date: 2024-10-30 07:50:05.997763

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0e04006c1c8b"
down_revision: Union[str, None] = "c84dd7a6c3ba"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_to_squads_views_association")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_to_squads_views_association",
        sa.Column(
            "squad_id", sa.INTEGER(), autoincrement=False, nullable=False
        ),
        sa.Column(
            "user_id", sa.INTEGER(), autoincrement=False, nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["squad_id"],
            ["squads.id"],
            name="user_to_squads_views_association_squad_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name="user_to_squads_views_association_user_id_fkey",
        ),
        sa.PrimaryKeyConstraint(
            "squad_id", "user_id", name="user_to_squads_views_association_pkey"
        ),
    )
    # ### end Alembic commands ###