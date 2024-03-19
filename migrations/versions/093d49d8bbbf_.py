"""empty message

Revision ID: 093d49d8bbbf
Revises: 581064224128
Create Date: 2024-03-19 15:43:13.401764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '093d49d8bbbf'
down_revision = '581064224128'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('release_date', sa.String(), nullable=True),
    sa.Column('overview', sa.Text(), nullable=True),
    sa.Column('poster_path', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('tmdb_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_movies_tmdb_id'), ['tmdb_id'], unique=True)

    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('review', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('ratings', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_ratings_movie_id'), ['movie_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_ratings_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ratings', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_ratings_user_id'))
        batch_op.drop_index(batch_op.f('ix_ratings_movie_id'))

    op.drop_table('ratings')
    op.drop_table('users')
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_movies_tmdb_id'))

    op.drop_table('movies')
    # ### end Alembic commands ###
