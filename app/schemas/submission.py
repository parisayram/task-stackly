from datetime import datetime
import json
from typing import Any, List

from pydantic import BaseModel, ConfigDict, field_validator

class SubmissionByForm(BaseModel):
    form_id: int
    submission_count: int


class SubmissionAnalyticsResponse(BaseModel):
    total_submissions: int
    today_submissions: int
    this_month_submissions: int
    unique_employees: int
    forms_with_submissions: int
    submissions_by_form: List[SubmissionByForm]


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
    def parse_data(cls, value: Any) -> Any:
        if isinstance(value, str):
            return json.loads(value)

        return value
