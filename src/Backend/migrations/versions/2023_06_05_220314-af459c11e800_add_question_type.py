"""Add question type

Revision ID: af459c11e800
Revises: a8fb190bf415
Create Date: 2023-06-05 22:03:14.109458+00:00

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "af459c11e800"
down_revision = "a8fb190bf415"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    question_type = postgresql.ENUM(
        "WORDS",
        "PHRASES",
        name="questiontype",
        create_type=False,
    )
    question_type.create(op.get_bind(), checkfirst=False)
    op.add_column(
        "questions",
        sa.Column(
            "type",
            postgresql.ENUM("WORDS", "PHRASES", name="questiontype"),
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("questions", "type")
    # ### end Alembic commands ###
