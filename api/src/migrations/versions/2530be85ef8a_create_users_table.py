"""create user table

Revision ID: 2530be85ef8a
Revises: 
Create Date: 2022-06-10 10:21:28.040523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2530be85ef8a'
down_revision = None
branch_labels = None
depends_on = None

""""
    Create the table product in database     
"""

def upgrade() -> None:
    op.create_table(
        'product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String(50), nullable=False),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('category', sa.String(50))
    ), 


def downgrade() -> None:
    op.drop_table('product')
