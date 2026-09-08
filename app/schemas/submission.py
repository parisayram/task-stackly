from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, ConfigDict


class SubmissionCreate(BaseModel):
    data: Dict[str, Any]  # {field_id: value}


class SubmissionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    form_id: int
    submitted_by: Optional[int] = None
    data: Dict[str, Any]
    status: str
    submitted_at: datetime
    updated_at: datetime


class ValidationError(BaseModel):
    field_id: int
    message: str


class ValidationResult(BaseModel):
    valid: bool
    errors: list[ValidationError] = []


class StatusUpdate(BaseModel):
    status: str
    note: Optional[str] = None


class StatusHistoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    submission_id: int
    status: str
    changed_by: Optional[int] = None
    changed_at: datetime
    note: Optional[str] = None
