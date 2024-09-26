"""Initial migration

Revision ID: 90dd0b9decf7
Revises: 
Create Date: 2024-09-21 12:06:05.941504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90dd0b9decf7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('vulnerability',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cve_id', sa.String(length=100), nullable=False),
    sa.Column('severity', sa.String(length=20), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vulnerability')
    op.drop_table('user')
    # ### end Alembic commands ###
