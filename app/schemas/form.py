from datetime import datetime
from pydantic import BaseModel


class FormCreate(BaseModel):
    name: str
    description: str | None = None


class FormUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class FormResponse(BaseModel):
    id: int
    name: str
    description: str | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True