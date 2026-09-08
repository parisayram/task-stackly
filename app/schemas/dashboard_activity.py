from datetime import datetime
from typing import List

from pydantic import BaseModel


class ActivityItem(BaseModel):
    activity_type: str
    submission_id: int
    form_id: int
    form_name: str
    employee_id: int
    employee_name: str
    occurred_at: datetime


class ActivityResponse(BaseModel):
    activities: List[ActivityItem]