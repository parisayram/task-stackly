from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DashboardSubmissionResponse(BaseModel):

    id: int

    form_id: int

    user_id: Optional[int] = None

    status: str

    submitted_at: datetime

    class Config:
        from_attributes = True


class DashboardFilterResponse(BaseModel):

    total_submissions: int

    pending_submissions: int

    approved_submissions: int

    rejected_submissions: int

    from_date: Optional[datetime] = None

    to_date: Optional[datetime] = None

    page: int

    page_size: int

    total_pages: int

    submissions: list[DashboardSubmissionResponse]