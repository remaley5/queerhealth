"""empty message

Revision ID: 8a52b49d563f
Revises: c604821d8ba0
Create Date: 2020-12-05 20:06:59.763050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a52b49d563f'
down_revision = 'c604821d8ba0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('relationship_preference_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'relationship_preference', ['relationship_preference_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'relationship_preference_id')
    # ### end Alembic commands ###