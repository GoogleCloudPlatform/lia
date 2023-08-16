"""Add column to result table

Revision ID: fcf319cac6bd
Revises: 494802acfeeb
Create Date: 2023-06-06 20:09:41.642601+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcf319cac6bd'
down_revision = '494802acfeeb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exams_users_questions', sa.Column('audio_url', sa.String(length=400), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('exams_users_questions', 'audio_url')
    # ### end Alembic commands ###