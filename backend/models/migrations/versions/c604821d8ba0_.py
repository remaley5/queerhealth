"""empty message

Revision ID: c604821d8ba0
Revises: da423adc7d76
Create Date: 2020-12-05 20:05:57.312150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c604821d8ba0'
down_revision = 'da423adc7d76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('relationship_preference', sa.Column('sexuality_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'relationship_preference', 'sexuality', ['sexuality_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'relationship_preference', type_='foreignkey')
    op.drop_column('relationship_preference', 'sexuality_id')
    # ### end Alembic commands ###
