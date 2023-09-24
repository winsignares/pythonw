"""Agregando nuevos atributos a la tabla Cliente

Revision ID: 6a632cab9adf
Revises: 
Create Date: 2023-09-20 15:40:22.995420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a632cab9adf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tblcliente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('correo', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('telefono', sa.String(length=10), nullable=True))
        batch_op.add_column(sa.Column('direccion', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tblcliente', schema=None) as batch_op:
        batch_op.drop_column('direccion')
        batch_op.drop_column('telefono')
        batch_op.drop_column('correo')

    # ### end Alembic commands ###
