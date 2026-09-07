from sqlalchemy.orm import Session

from app.models.submission import Submission


def create_submission(
    db: Session,
    form_id: int,
    employee_id: int,
    data: str
):
    submission = Submission(
        form_id=form_id,
        employee_id=employee_id,
        data=data
    )

    db.add(submission)
    db.commit()
    db.refresh(submission)

    return submission


def get_submission(
    db: Session,
    submission_id: int
):
    return (
        db.query(Submission)
        .filter(Submission.id == submission_id)
        .first()
    )


def get_submissions_by_form(
    db: Session,
    form_id: int
):
    return (
        db.query(Submission)
        .filter(Submission.form_id == form_id)
        .all()
    )


def get_submissions_by_employee(
    db: Session,
    employee_id: int
):
    return (
        db.query(Submission)
        .filter(Submission.employee_id == employee_id)
        .all()
    )