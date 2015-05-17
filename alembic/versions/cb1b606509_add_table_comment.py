"""add table comment

Revision ID: cb1b606509
Revises: 1a391246b1e5
Create Date: 2015-05-15 21:40:33.270410

"""

# revision identifiers, used by Alembic.
revision = 'cb1b606509'
down_revision = '1a391246b1e5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'comment',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('author_id', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('issue_id', sa.Integer, sa.ForeignKey('issue.id')),
        sa.Column('message', sa.String(400), nullable=False),
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
        pass
    ### end Alembic commands ###
