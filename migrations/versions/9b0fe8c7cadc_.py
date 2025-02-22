"""empty message

Revision ID: 9b0fe8c7cadc
Revises: 161ad4e57543
Create Date: 2021-11-03 15:49:13.820131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b0fe8c7cadc'
down_revision = '161ad4e57543'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['goal_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###
