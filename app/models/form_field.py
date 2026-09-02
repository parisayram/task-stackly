from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Text
)

from app.database import Base


class FormField(Base):
    __tablename__ = "form_fields"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    form_id = Column(
        Integer,
        ForeignKey("forms.id", ondelete="CASCADE"),
        nullable=False
    )

    field_name = Column(
        String(100),
        nullable=False
    )

    field_type = Column(
        String(50),
        nullable=False
    )

    label = Column(
        String(150),
        nullable=False
    )

    placeholder = Column(
        String(200),
        nullable=True
    )

    is_required = Column(
        Boolean,
        default=False
    )

    options = Column(
        Text,
        nullable=True
    )