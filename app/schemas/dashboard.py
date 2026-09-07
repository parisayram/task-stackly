from pydantic import BaseModel
from typing import List


class FormDetailStatistics(BaseModel):
    form_id: int
    form_name: str
    submission_count: int


class FormStatisticsResponse(BaseModel):
    total_forms: int
    total_submissions: int
    forms_with_submissions: int
    forms_without_submissions: int
    forms: List[FormDetailStatistics]