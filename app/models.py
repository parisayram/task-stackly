from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from .database import Base


class Form(Base):

    __tablename__ = "forms"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    status = Column(
        String(30),
        default="active",
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )


class Submission(Base):

    __tablename__ = "submissions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    form_id = Column(
        Integer,
        ForeignKey("forms.id"),
        nullable=False,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=True,
        index=True
    )

    status = Column(
        String(30),
        default="pending",
        nullable=False,
        index=True
    )

    submitted_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True
    )