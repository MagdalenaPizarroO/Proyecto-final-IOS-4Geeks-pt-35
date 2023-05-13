"""empty message

Revision ID: b7de27db864c
Revises: 859fcfbd00c5
Create Date: 2023-05-11 19:42:26.348104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7de27db864c'
down_revision = '859fcfbd00c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.alter_column('telefono',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.alter_column('telefono',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###