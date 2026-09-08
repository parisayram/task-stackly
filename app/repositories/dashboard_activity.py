from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.models.form import Form
from app.models.submission import Submission


def get_recent_activity(db: Session, limit: int):
    rows = (
        db.query(Submission, Form, Employee)
        .join(Form, Form.id == Submission.form_id)
        .join(Employee, Employee.employee_id == Submission.employee_id)
        .order_by(Submission.submitted_at.desc(), Submission.id.desc())
        .limit(limit)
        .all()
    )

    return [
        {
            "activity_type": "submission",
            "submission_id": submission.id,
            "form_id": form.id,
            "form_name": form.name,
            "employee_id": employee.employee_id,
            "employee_name": employee.name,
            "occurred_at": submission.submitted_at,
        }
        for submission, form, employee in rows
    ]