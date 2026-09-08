"""
Minimal User table so FKs across Forms/Dashboard resolve.
If your team already has a separate Auth service/table, replace this
with an import from that module — keep the table name "users" and the
columns below so nothing else breaks.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
