from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class FormBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: bool = True


class FormCreate(FormBase):
    pass


class FormUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class FormOut(FormBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_by: Optional[int] = None
    created_at: datetime
    updated_at: datetime
