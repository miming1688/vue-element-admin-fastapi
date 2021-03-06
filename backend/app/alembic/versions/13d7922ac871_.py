"""

Revision ID: 13d7922ac871
Revises: 3161ae076013
Create Date: 2020-07-08 23:28:31.418954

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '13d7922ac871'
down_revision = '3161ae076013'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu', sa.Column('external_link', sa.Boolean(), nullable=True))
    op.drop_column('menu', 'is_frame')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu', sa.Column('is_frame', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('menu', 'external_link')
    # ### end Alembic commands ###
