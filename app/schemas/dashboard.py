from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_forms: int
    total_submissions: int
    total_users: int
    active_forms: int


class UserStats(BaseModel):
    total_users: int
    active_users: int
    new_users_last_7_days: int


class FormStats(BaseModel):
    form_id: int
    title: str
    submission_count: int
    active: bool


class SubmissionAnalytics(BaseModel):
    total_submissions: int
    submissions_by_status: Dict[str, int]
    submissions_over_time: List[Dict[str, Any]]  # [{date: ..., count: ...}]


class ActivityItem(BaseModel):
    type: str  # "form_created", "submission_received", etc.
    description: str
    timestamp: datetime
    actor_id: Optional[int] = None


class DateRangeFilter(BaseModel):
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    form_id: Optional[int] = None
    status: Optional[str] = None


class ExportRequest(BaseModel):
    format: str = "csv"  # csv | json
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
