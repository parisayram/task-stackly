"""Owner: Kallam Poojitha (Form CRUD) — extend here, don't fork a new table."""

from datetime import datetime

from sqlalchemy import Column, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import relationship

from app.database import Base


class Form(Base):
    __tablename__ = "forms"

    id = Column(
        BIGINT(unsigned=True),
        primary_key=True,
        index=True
    )

    title = Column(
        String(255),
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_by = Column(
        BIGINT(unsigned=True),
        ForeignKey("users.id"),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    fields = relationship(
        "FormField",
        back_populates="form",
        cascade="all, delete-orphan"
    )

    submissions = relationship(
        "FormSubmission",
        back_populates="form",
        cascade="all, delete-orphan"
    )

    permissions = relationship(
        "FormPermission",
        back_populates="form",
        cascade="all, delete-orphan"
    )