from typing import Optional, Any, Dict
from pydantic import BaseModel, ConfigDict


class FieldBase(BaseModel):
    label: str
    field_type: str
    is_required: bool = False
    order: int = 0
    options: Optional[list] = None
    validation_rules: Optional[Dict[str, Any]] = None


class FieldCreate(FieldBase):
    pass


class FieldUpdate(BaseModel):
    label: Optional[str] = None
    field_type: Optional[str] = None
    is_required: Optional[bool] = None
    order: Optional[int] = None
    options: Optional[list] = None
    validation_rules: Optional[Dict[str, Any]] = None


class FieldOut(FieldBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    form_id: int
