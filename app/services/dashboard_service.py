"""
Dashboard services — split by owner but kept in one file since each
function is small. Feel free to split into per-owner files if it grows.
"""
import csv
import io
from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session

from app.repositories import dashboard_repository as repo
from app.schemas.dashboard import (
    DashboardSummary, UserStats, FormStats, SubmissionAnalytics, DateRangeFilter,
)


def get_summary(db: Session) -> DashboardSummary:
    """Owner: Anoop P."""
    return DashboardSummary(
        total_forms=repo.count_forms(db),
        total_submissions=repo.count_submissions(db),
        total_users=repo.count_users(db),
        active_forms=repo.count_active_forms(db),
    )


def get_user_stats(db: Session) -> UserStats:
    """Owner: ARAGONDA NIKHIL."""
    since = datetime.utcnow() - timedelta(days=7)
    return UserStats(
        total_users=repo.count_users(db),
        active_users=repo.count_active_users(db),
        new_users_last_7_days=repo.count_new_users_since(db, since),
    )


def get_form_stats(db: Session) -> list[FormStats]:
    """Owner: Chintha Gayathri."""
    rows = repo.form_stats(db)
    return [
        FormStats(form_id=r.id, title=r.title, submission_count=r.submission_count, active=r.is_active)
        for r in rows
    ]


def get_submission_analytics(db: Session, days: int = 30) -> SubmissionAnalytics:
    """Owner: Ilavarasan Palanisamy."""
    return SubmissionAnalytics(
        total_submissions=repo.count_submissions(db),
        submissions_by_status=repo.submissions_by_status(db),
        submissions_over_time=repo.submissions_over_time(db, days),
    )


def apply_filters(db: Session, filters: DateRangeFilter):
    """Owner: Kishore A — Dashboard Filters & Date Range."""
    return repo.filtered_submissions(
        db,
        start_date=filters.start_date,
        end_date=filters.end_date,
        form_id=filters.form_id,
        status=filters.status,
    )


def export_submissions(
    db: Session,
    fmt: str = "csv",
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
) -> str:
    """Owner: V Deepa — Export/Report API + overall testing."""
    submissions = repo.filtered_submissions(db, start_date=start_date, end_date=end_date)

    if fmt == "json":
        import json
        return json.dumps(
            [
                {
                    "id": s.id, "form_id": s.form_id, "status": s.status,
                    "submitted_at": s.submitted_at.isoformat(), "data": s.data,
                }
                for s in submissions
            ]
        )

    # default: csv
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["id", "form_id", "status", "submitted_at", "data"])
    for s in submissions:
        writer.writerow([s.id, s.form_id, s.status, s.submitted_at.isoformat(), s.data])
    return output.getvalue()
