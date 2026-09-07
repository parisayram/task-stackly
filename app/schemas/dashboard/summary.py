from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_employees: int
    active_employees: int
    total_forms: int
    total_submissions: int