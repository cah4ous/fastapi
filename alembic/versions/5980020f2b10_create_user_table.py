"""create user table

Revision ID: 5980020f2b10
Revises: 
Create Date: 2021-07-14 12:07:28.177380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5980020f2b10'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('username', sa.String(50), unique=True),
        sa.Column('hashed_password', sa.String(200)),
        sa.Column('email', sa.String(200)),
        sa.Column('is_active', sa.Boolean),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    pass
