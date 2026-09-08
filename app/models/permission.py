"""Owner: TeamStackly — Form Permissions / Access Control."""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import relationship

from app.database import Base


class FormPermission(Base):
    __tablename__ = "form_permissions"

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

    user_id = Column(
        BIGINT(unsigned=True),
        ForeignKey("users.id"),
        nullable=False
    )

    role = Column(
        String(50),
        nullable=True
    )

    form = relationship(
        "Form",
        back_populates="permissions"
    )