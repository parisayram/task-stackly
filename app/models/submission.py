"""Owner: Sheetal (Form Submission APIs) & Sumanth M T (History & Status)."""

from datetime import datetime

from sqlalchemy import Column, String, JSON, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import relationship

from app.database import Base


class FormSubmission(Base):
    __tablename__ = "form_submissions"

    id = Column(
        BIGINT(unsigned=True),
        primary_key=True,
        index=True
    )

    form_id = Column(
        BIGINT(unsigned=True),
        ForeignKey("forms.id"),
        nullable=False
    )

    submitted_by = Column(
        BIGINT(unsigned=True),
        ForeignKey("users.id"),
        nullable=True
    )

    data = Column(JSON, nullable=False)

    status = Column(
        String(50),
        default="submitted"
    )

    submitted_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    form = relationship(
        "Form",
        back_populates="submissions"
    )

    status_history = relationship(
        "SubmissionStatusHistory",
        back_populates="submission",
        cascade="all, delete-orphan"
    )


class SubmissionStatusHistory(Base):
    """Used by Sumanth M T's Submission History & Status API."""

    __tablename__ = "submission_status_history"

    id = Column(
        BIGINT(unsigned=True),
        primary_key=True,
        index=True
    )

    submission_id = Column(
        BIGINT(unsigned=True),
        ForeignKey("form_submissions.id"),
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False
    )

    changed_by = Column(
        BIGINT(unsigned=True),
        ForeignKey("users.id"),
        nullable=True
    )

    changed_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    note = Column(
        String(500),
        nullable=True
    )

    submission = relationship(
        "FormSubmission",
        back_populates="status_history"
    )