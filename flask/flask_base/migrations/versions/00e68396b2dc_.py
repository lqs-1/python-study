"""empty message

Revision ID: 00e68396b2dc
Revises: 
Create Date: 2022-01-11 17:26:07.901986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00e68396b2dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
