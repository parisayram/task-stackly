from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FormCreate(BaseModel):
    name: str
    description: Optional[str] = None
    created_by: int
    status: str = "active"


class FormUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None


class FormResponse(BaseModel):
    form_id: int
    name: str
    description: Optional[str]
    created_by: int
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
