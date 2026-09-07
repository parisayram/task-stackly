from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.form import Form
from app.models.submission import Submission


def get_form_statistics(db: Session):
    # Total number of forms
    total_forms = db.query(func.count(Form.id)).scalar() or 0

    # Total number of submissions
    total_submissions = db.query(func.count(Submission.id)).scalar() or 0

    # Number of forms that have at least one submission
    forms_with_submissions = (
        db.query(func.count(func.distinct(Submission.form_id)))
        .scalar()
        or 0
    )

    # Number of forms without submissions
    forms_without_submissions = total_forms - forms_with_submissions

    # Submission count for each form
    form_submission_counts = (
        db.query(
            Form.id,
            Form.name,
            func.count(Submission.id).label("submission_count")
        )
        .outerjoin(
            Submission,
            Form.id == Submission.form_id
        )
        .group_by(Form.id, Form.name)
        .all()
    )

    forms = [
        {
            "form_id": form_id,
            "form_name": form_name,
            "submission_count": submission_count
        }
        for form_id, form_name, submission_count in form_submission_counts
    ]

    return {
        "total_forms": total_forms,
        "total_submissions": total_submissions,
        "forms_with_submissions": forms_with_submissions,
        "forms_without_submissions": forms_without_submissions,
        "forms": forms
    }