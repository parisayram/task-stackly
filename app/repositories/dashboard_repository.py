from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.form import Form
from app.models.submission import FormSubmission
from app.models.user import User


def count_forms(db: Session) -> int:
    return db.query(func.count(Form.id)).scalar()


def count_active_forms(db: Session) -> int:
    return db.query(func.count(Form.id)).filter(Form.is_active.is_(True)).scalar()


def count_submissions(db: Session) -> int:
    return db.query(func.count(FormSubmission.id)).scalar()


def count_users(db: Session) -> int:
    return db.query(func.count(User.id)).scalar()


def count_active_users(db: Session) -> int:
    return db.query(func.count(User.id)).filter(User.is_active.is_(True)).scalar()


def count_new_users_since(db: Session, since: datetime) -> int:
    return db.query(func.count(User.id)).filter(User.created_at >= since).scalar()


def form_stats(db: Session):
    """Submission count per form, for Chintha Gayathri's Form Statistics API."""
    return (
        db.query(Form.id, Form.title, Form.is_active, func.count(FormSubmission.id).label("submission_count"))
        .outerjoin(FormSubmission, FormSubmission.form_id == Form.id)
        .group_by(Form.id)
        .all()
    )


def submissions_by_status(db: Session):
    rows = (
        db.query(FormSubmission.status, func.count(FormSubmission.id))
        .group_by(FormSubmission.status)
        .all()
    )
    return {status: count for status, count in rows}


def submissions_over_time(db: Session, days: int = 30):
    """Daily submission counts for the last N days — Ilavarasan's Analytics API."""
    since = datetime.utcnow() - timedelta(days=days)
    rows = (
        db.query(func.date(FormSubmission.submitted_at), func.count(FormSubmission.id))
        .filter(FormSubmission.submitted_at >= since)
        .group_by(func.date(FormSubmission.submitted_at))
        .order_by(func.date(FormSubmission.submitted_at))
        .all()
    )
    return [{"date": str(d), "count": c} for d, c in rows]


def filtered_submissions(
    db: Session,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    form_id: Optional[int] = None,
    status: Optional[str] = None,
):
    """Used by both Kishore's Filters API and Deepa's Export API."""
    query = db.query(FormSubmission)
    if start_date:
        query = query.filter(FormSubmission.submitted_at >= start_date)
    if end_date:
        query = query.filter(FormSubmission.submitted_at <= end_date)
    if form_id:
        query = query.filter(FormSubmission.form_id == form_id)
    if status:
        query = query.filter(FormSubmission.status == status)
    return query.order_by(FormSubmission.submitted_at.desc()).all()
