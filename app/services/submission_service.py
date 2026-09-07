import json

from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.models.form import Form
from app.repositories import submission_repository
from app.schemas.submission import SubmissionCreate


def create_submission(
    db: Session,
    submission: SubmissionCreate
):
    form = (
        db.query(Form)
        .filter(Form.id == submission.form_id)
        .first()
    )

    if not form:
        raise ValueError("Form not found")

    employee = (
        db.query(Employee)
        .filter(Employee.employee_id == submission.employee_id)
        .first()
    )

    if not employee:
        raise ValueError("Employee not found")

    submission_data = json.dumps(submission.data)

    return submission_repository.create_submission(
        db=db,
        form_id=submission.form_id,
        employee_id=submission.employee_id,
        data=submission_data
    )


def get_submission(
    db: Session,
    submission_id: int
):
    submission = submission_repository.get_submission(
        db,
        submission_id
    )

    if not submission:
        raise ValueError("Submission not found")

    return submission


def get_submissions_by_form(
    db: Session,
    form_id: int
):
    return submission_repository.get_submissions_by_form(
        db,
        form_id
    )


def get_submissions_by_employee(
    db: Session,
    employee_id: int
):
    return submission_repository.get_submissions_by_employee(
        db,
        employee_id
    )