"""Owner: Kadirimangalam (Form Fields APIs)."""
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.database import Base


class FormField(Base):
    __tablename__ = "form_fields"

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)
    label = Column(String(255), nullable=False)
    field_type = Column(String(50), nullable=False)
    is_required = Column(Boolean, default=False)

    order = Column("field_order", Integer, default=0)

    options = Column(JSON, nullable=True)
    validation_rules = Column(JSON, nullable=True)

    form = relationship("Form", back_populates="fields")
