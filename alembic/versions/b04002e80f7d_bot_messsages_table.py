"""Bot Messsages Table

Revision ID: b04002e80f7d
Revises: 01cffc7b13aa
Create Date: 2021-07-26 14:46:48.960252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b04002e80f7d'
down_revision = '01cffc7b13aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bot_messages',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('message_id'),
    sa.UniqueConstraint('name')
    )
    op.create_unique_constraint(None, 'bot_version', ['version'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bot_version', type_='unique')
    op.drop_table('bot_messages')
    # ### end Alembic commands ###
