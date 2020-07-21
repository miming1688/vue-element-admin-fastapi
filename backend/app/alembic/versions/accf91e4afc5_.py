"""

Revision ID: accf91e4afc5
Revises: bcdec3973818
Create Date: 2020-06-26 17:05:50.331296

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'accf91e4afc5'
down_revision = 'bcdec3973818'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu', sa.Column('affix', sa.Boolean(), nullable=True))
    op.add_column('menu', sa.Column('component', sa.String(length=32), nullable=True))
    op.add_column('menu', sa.Column('hidden', sa.Boolean(), nullable=True))
    op.add_column('menu', sa.Column('icon', sa.String(length=32), nullable=True))
    op.add_column('menu', sa.Column('noCache', sa.Boolean(), nullable=True))
    op.add_column('menu', sa.Column('redirect', sa.String(length=32), nullable=True))
    op.add_column('menu', sa.Column('title', sa.String(length=32), nullable=True))
    op.alter_column('menu', 'path',
               existing_type=mysql.VARCHAR(length=32),
               type_=sa.String(length=128),
               existing_nullable=True)
    op.create_index(op.f('ix_menu_parent_id'), 'menu', ['parent_id'], unique=False)
    op.drop_index('ix_menu_path', table_name='menu')
    op.drop_column('menu', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu', sa.Column('name', mysql.VARCHAR(length=32), nullable=True))
    op.create_index('ix_menu_path', 'menu', ['path'], unique=False)
    op.drop_index(op.f('ix_menu_parent_id'), table_name='menu')
    op.alter_column('menu', 'path',
               existing_type=sa.String(length=128),
               type_=mysql.VARCHAR(length=32),
               existing_nullable=True)
    op.drop_column('menu', 'title')
    op.drop_column('menu', 'redirect')
    op.drop_column('menu', 'noCache')
    op.drop_column('menu', 'icon')
    op.drop_column('menu', 'hidden')
    op.drop_column('menu', 'component')
    op.drop_column('menu', 'affix')
    # ### end Alembic commands ###