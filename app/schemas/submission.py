from datetime import datetime
from typing import Any
import json

from pydantic import BaseModel, ConfigDict, field_validator


class SubmissionCreate(BaseModel):
    form_id: int
    employee_id: int
    data: dict[str, Any]


class SubmissionResponse(BaseModel):
    id: int
    form_id: int
    employee_id: int
    data: dict[str, Any]
    submitted_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @field_validator("data", mode="before")
    @classmethod
    def parse_data(cls, value):
        if isinstance(value, str):
            return json.loads(value)

        return value