from typing import Optional
from sqlalchemy.orm import Session

from app.models.submission import FormSubmission, SubmissionStatusHistory
from app.schemas.submission import SubmissionCreate


def create_submission(
    db: Session, form_id: int, data: SubmissionCreate, submitted_by: Optional[int] = None
) -> FormSubmission:
    submission = FormSubmission(
        form_id=form_id, data=data.data, submitted_by=submitted_by, status="submitted"
    )
    db.add(submission)
    db.commit()
    db.refresh(submission)
    # first row of history so status is auditable from creation
    add_status_history(db, submission.id, "submitted", submitted_by, note="Initial submission")
    return submission


def get_submission(db: Session, form_id: int, submission_id: int) -> Optional[FormSubmission]:
    return db.query(FormSubmission).filter(
        FormSubmission.id == submission_id, FormSubmission.form_id == form_id
    ).first()


def list_submissions(db: Session, form_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(FormSubmission)
        .filter(FormSubmission.form_id == form_id)
        .order_by(FormSubmission.submitted_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_status(db: Session, submission: FormSubmission, status: str) -> FormSubmission:
    submission.status = status
    db.commit()
    db.refresh(submission)
    return submission


def add_status_history(
    db: Session, submission_id: int, status: str, changed_by: Optional[int] = None, note: Optional[str] = None
) -> SubmissionStatusHistory:
    entry = SubmissionStatusHistory(
        submission_id=submission_id, status=status, changed_by=changed_by, note=note
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def get_status_history(db: Session, submission_id: int):
    return (
        db.query(SubmissionStatusHistory)
        .filter(SubmissionStatusHistory.submission_id == submission_id)
        .order_by(SubmissionStatusHistory.changed_at)
        .all()
    )
