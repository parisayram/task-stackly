from sqlalchemy import Column, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.sql import func

from app.database import Base


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    form_id = Column(
        Integer,
        ForeignKey("forms.id", ondelete="CASCADE"),
        nullable=False
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id", ondelete="CASCADE"),
        nullable=False
    )

    data = Column(
        Text,
        nullable=False
    )

    submitted_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        nullable=False
    )