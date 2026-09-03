from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer

from app.database import Base


class FormPermission(Base):
    __tablename__ = "form_permissions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    form_id = Column(
        Integer,
        ForeignKey("forms.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    can_view = Column(
        Boolean,
        default=True,
        nullable=False
    )

    can_submit = Column(
        Boolean,
        default=False,
        nullable=False
    )

    can_edit = Column(
        Boolean,
        default=False,
        nullable=False
    )

    can_delete = Column(
        Boolean,
        default=False,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )