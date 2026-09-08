"""Owner: K Parisayram (Recent Activity API)."""
from sqlalchemy.orm import Session

from app.models.form import Form
from app.models.submission import FormSubmission
from app.schemas.dashboard import ActivityItem


def get_recent_activity(db: Session, limit: int = 20) -> list[ActivityItem]:
    activity = []

    recent_forms = db.query(Form).order_by(Form.created_at.desc()).limit(limit).all()
    for f in recent_forms:
        activity.append(
            ActivityItem(
                type="form_created",
                description=f"Form '{f.title}' was created",
                timestamp=f.created_at,
                actor_id=f.created_by,
            )
        )

    recent_submissions = db.query(FormSubmission).order_by(FormSubmission.submitted_at.desc()).limit(limit).all()
    for s in recent_submissions:
        activity.append(
            ActivityItem(
                type="submission_received",
                description=f"New submission on form #{s.form_id}",
                timestamp=s.submitted_at,
                actor_id=s.submitted_by,
            )
        )

    activity.sort(key=lambda a: a.timestamp, reverse=True)
    return activity[:limit]
