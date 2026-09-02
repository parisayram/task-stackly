from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.sql import func

from app.database import Base


class Form(Base):
    __tablename__ = "forms"

    form_id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(150), nullable=False)

    description = Column(Text, nullable=True)

    created_by = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=False
    )

    status = Column(
        Enum("active", "inactive"),
        nullable=False,
        default="active"
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )
