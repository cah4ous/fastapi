"""create post table

Revision ID: cff1e26681d3
Revises: 5a93821c2e12
Create Date: 2021-07-14 15:46:46.193028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cff1e26681d3'
down_revision = '5a93821c2e12'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('title', sa.String(50)),
        sa.Column('body', sa.String(1000)),
        sa.Column('email', sa.String(200)),
        sa.Column('is_active', sa.Boolean),
        sa.Column('owner_id', sa.Integer)
    )


def downgrade():
    pass
