"""Owner: Sheetal (Submission) + Sumanth M T (History & Status)."""
from typing import Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import submission_repository
from app.services.form_service import get_form_or_404
from app.services.validation_service import validate_submission
from app.schemas.submission import SubmissionCreate, StatusUpdate


def create_submission(db: Session, form_id: int, data: SubmissionCreate, submitted_by: Optional[int] = None):
    get_form_or_404(db, form_id)

    result = validate_submission(db, form_id, data.data)
    if not result.valid:
        raise HTTPException(status_code=422, detail=[e.model_dump() for e in result.errors])

    return submission_repository.create_submission(db, form_id, data, submitted_by)


def get_submission_or_404(db: Session, form_id: int, submission_id: int):
    submission = submission_repository.get_submission(db, form_id, submission_id)
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")
    return submission


def list_submissions(db: Session, form_id: int, skip: int = 0, limit: int = 100):
    get_form_or_404(db, form_id)
    return submission_repository.list_submissions(db, form_id, skip, limit)


def update_status(db: Session, form_id: int, submission_id: int, payload: StatusUpdate, changed_by: Optional[int] = None):
    submission = get_submission_or_404(db, form_id, submission_id)
    updated = submission_repository.update_status(db, submission, payload.status)
    submission_repository.add_status_history(db, submission.id, payload.status, changed_by, payload.note)
    return updated


def get_history(db: Session, form_id: int, submission_id: int):
    get_submission_or_404(db, form_id, submission_id)
    return submission_repository.get_status_history(db, submission_id)
