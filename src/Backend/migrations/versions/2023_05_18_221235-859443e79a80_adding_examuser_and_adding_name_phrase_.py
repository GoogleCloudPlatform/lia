"""Adding ExamUser and adding name/phrase_id to Question

Revision ID: 859443e79a80
Revises: 03adf77cecd0
Create Date: 2023-05-18 22:12:35.145550+00:00

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "859443e79a80"
down_revision = "03adf77cecd0"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "exams_users",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("exam_id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column(
            "status",
            postgresql.ENUM(
                "NOT_STARTED", "IN_PROGRESS", "FINISHED", name="examstatus"
            ),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["exam_id"],
            ["exams.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id", "exam_id", "user_id"),
    )
    op.add_column("questions", sa.Column("name", sa.String(length=50), nullable=False))
    op.add_column(
        "questions", sa.Column("phrase_id", sa.String(length=100), nullable=False)
    )
    op.drop_constraint(
        "exams_users_questions_organization_id_fkey",
        "exams_users_questions",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "exams_users_questions",
        "groups",
        ["organization_id"],
        ["id"],
        ondelete="RESTRICT",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "exams_users_questions", type_="foreignkey")
    op.create_foreign_key(
        "exams_users_questions_organization_id_fkey",
        "exams_users_questions",
        "organizations",
        ["organization_id"],
        ["id"],
        ondelete="RESTRICT",
    )
    op.drop_column("questions", "phrase_id")
    op.drop_column("questions", "name")
    op.drop_table("exams_users")
    # ### end Alembic commands ###
