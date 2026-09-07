<<<<<<< HEAD
from pydantic import BaseModel
from typing import List


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
    
=======
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
    def parse_data(cls, value: Any) -> Any:
        if isinstance(value, str):
            return json.loads(value)

        return value
>>>>>>> f4bafd5357a1426f490c1195c11414eeeb5b67b4
