"""add Vote model

Revision ID: 47193e9cc561
Revises: eac750d860b
Create Date: 2015-06-10 00:17:22.466285

"""

# revision identifiers, used by Alembic.
revision = '47193e9cc561'
down_revision = 'eac750d860b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('vote', sa.Boolean(), nullable=True),
    sa.Column('target_type', sa.Unicode(length=255), nullable=True),
    sa.Column('target_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('idx_issue_coordinates', table_name='issue')
    op.drop_index('idx_organization_address', table_name='organization')
    op.drop_constraint(u'user_organization_fkey', 'user', type_='foreignkey')
    op.drop_column(u'user', 'organization')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'user', sa.Column('organization', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'user_organization_fkey', 'user', 'organization', ['organization'], ['id'])
    op.create_index('idx_organization_address', 'organization', ['address'], unique=False)
    op.create_index('idx_issue_coordinates', 'issue', ['coordinates'], unique=False)
    op.drop_table('vote')
    ### end Alembic commands ###
