"""empty message

Revision ID: c5666b76620b
Revises: a6821791ca92
Create Date: 2018-08-08 11:50:20.615143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5666b76620b'
down_revision = 'a6821791ca92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('warings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('max', sa.Float(), nullable=True),
    sa.Column('min', sa.Float(), nullable=True),
    sa.Column('data', sa.Float(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.Column('sensor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['device_id'], ['devices.id'], ),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('sensor', sa.Column('max', sa.Float(), nullable=True))
    op.add_column('sensor', sa.Column('min', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sensor', 'min')
    op.drop_column('sensor', 'max')
    op.drop_table('warings')
    # ### end Alembic commands ###