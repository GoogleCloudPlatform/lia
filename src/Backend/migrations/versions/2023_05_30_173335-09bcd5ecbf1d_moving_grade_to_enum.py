"""Moving grade to enum

Revision ID: 09bcd5ecbf1d
Revises: 4a191094de13
Create Date: 2023-05-30 17:33:35.167663+00:00

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql as psql

# revision identifiers, used by Alembic.
revision = "09bcd5ecbf1d"
down_revision = "4a191094de13"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    grades_enum = psql.ENUM(
        "FIRST_FUND",
        "SECOND_FUND",
        "THIRD_FUND",
        "FOURTH_FUND",
        "FIFTH_FUND",
        "SIXTH_FUND",
        "SEVENTH_FUND",
        "EIGHTH_FUND",
        "NINETH_FUND",
        "FIRST_HS",
        "SECOND_HS",
        "THIRD_HS",
        name="grades",
        create_type=False,
    )
    grades_enum.create(op.get_bind(), checkfirst=False)
    op.add_column(
        "exams", sa.Column("start_date", sa.DateTime(timezone=True), nullable=False)
    )
    op.add_column(
        "exams", sa.Column("end_date", sa.DateTime(timezone=True), nullable=False)
    )
    op.drop_column("groups", "grade")
    op.add_column("groups", sa.Column("grade", grades_enum, nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "groups",
        sa.Column("grade", sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    )
    op.drop_column("exams", "end_date")
    op.drop_column("exams", "start_date")
    op.alter_column("groups", "grade", existing_type=sa.String(100), nullable=False)
    # ### end Alembic commands ###