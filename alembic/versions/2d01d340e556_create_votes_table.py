"""create votes table

Revision ID: 2d01d340e556
Revises: fe91257c8f32
Create Date: 2022-10-04 11:15:52.345196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d01d340e556'
down_revision = 'fe91257c8f32'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'votes',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('user_id', 'post_id')
    )

    pass


def downgrade() -> None:
    op.drop_table('votes')
    pass
