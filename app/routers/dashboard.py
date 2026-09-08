"""
Dashboard Group router — all 7 people's endpoints. Same rule as
forms.py: your endpoint calls your own service function.
"""
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.dashboard import (
    DashboardSummary, UserStats, FormStats, SubmissionAnalytics, ActivityItem, DateRangeFilter,
)
from app.services import dashboard_service, activity_service

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


# ---- Anoop P: Dashboard Summary API ----
@router.get("/summary", response_model=DashboardSummary)
def get_summary(db: Session = Depends(get_db)):
    return dashboard_service.get_summary(db)


# ---- ARAGONDA NIKHIL: User Statistics API ----
@router.get("/users", response_model=UserStats)
def get_user_stats(db: Session = Depends(get_db)):
    return dashboard_service.get_user_stats(db)


# ---- Chintha Gayathri: Form Statistics API ----
@router.get("/forms", response_model=list[FormStats])
def get_form_stats(db: Session = Depends(get_db)):
    return dashboard_service.get_form_stats(db)


# ---- Ilavarasan Palanisamy: Submission Analytics API ----
@router.get("/submissions", response_model=SubmissionAnalytics)
def get_submission_analytics(days: int = 30, db: Session = Depends(get_db)):
    return dashboard_service.get_submission_analytics(db, days)


# ---- K Parisayram: Recent Activity API ----
@router.get("/activity", response_model=list[ActivityItem])
def get_recent_activity(limit: int = 20, db: Session = Depends(get_db)):
    return activity_service.get_recent_activity(db, limit)


# ---- Kishore A: Dashboard Filters & Date Range ----
@router.get("/filters")
def apply_filters(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    form_id: Optional[int] = None,
    status: Optional[str] = None,
    db: Session = Depends(get_db),
):
    filters = DateRangeFilter(start_date=start_date, end_date=end_date, form_id=form_id, status=status)
    results = dashboard_service.apply_filters(db, filters)
    return {"count": len(results), "results": results}


# ---- V Deepa: Dashboard Export/Report API + Testing ----
@router.get("/export")
def export_report(
    format: str = Query("csv", pattern="^(csv|json)$"),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db),
):
    content = dashboard_service.export_submissions(db, format, start_date, end_date)
    media_type = "text/csv" if format == "csv" else "application/json"
    filename = f"submissions_export.{format}"
    return Response(
        content=content,
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
