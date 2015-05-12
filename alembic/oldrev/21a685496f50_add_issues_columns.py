"""add issues columns

Revision ID: 21a685496f50
Revises: 137bec66f203
Create Date: 2015-05-12 10:02:36.765733

"""

# revision identifiers, used by Alembic.
revision = '21a685496f50'
down_revision = '137bec66f203'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('issues')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('issues',
    sa.Column('id', sa.INTEGER(), server_default="nextval('issues_id_seq'::regclass)", nullable=False),
    sa.Column('reporter', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['reporter'], [u'user.id'], name=u'issues_reporter_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'issues_pkey')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), server_default="nextval('user_id_seq'::regclass)", nullable=False),
    sa.Column('fb_first_name', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('fb_last_name', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('fb_id', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'user_pkey'),
    sa.UniqueConstraint('email', name=u'user_email_key'),
    sa.UniqueConstraint('fb_id', name=u'user_fb_id_key')
    )
    ### end Alembic commands ###
