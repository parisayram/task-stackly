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
    