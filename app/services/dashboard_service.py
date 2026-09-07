from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.submission import Submission


def get_submission_analytics(db: Session):

    # Total number of submissions
    total_submissions = (
        db.query(func.count(Submission.id))
        .scalar()
    ) or 0

    # Today's submissions
    today_submissions = (
        db.query(func.count(Submission.id))
        .filter(
            func.date(Submission.submitted_at)
            == datetime.now().date()
        )
        .scalar()
    ) or 0

    # Current month's submissions
    this_month_submissions = (
        db.query(func.count(Submission.id))
        .filter(
            func.year(Submission.submitted_at)
            == datetime.now().year,
            func.month(Submission.submitted_at)
            == datetime.now().month
        )
        .scalar()
    ) or 0

    # Number of unique employees who submitted forms
    unique_employees = (
        db.query(
            func.count(
                func.distinct(Submission.employee_id)
            )
        )
        .scalar()
    ) or 0

    # Number of forms that have submissions
    forms_with_submissions = (
        db.query(
            func.count(
                func.distinct(Submission.form_id)
            )
        )
        .scalar()
    ) or 0

    # Submission count grouped by form
    submissions_by_form = (
        db.query(
            Submission.form_id,
            func.count(Submission.id).label("submission_count")
        )
        .group_by(Submission.form_id)
        .order_by(Submission.form_id)
        .all()
    )

    form_statistics = [
        {
            "form_id": form_id,
            "submission_count": submission_count
        }
        for form_id, submission_count in submissions_by_form
    ]

    return {
        "total_submissions": total_submissions,
        "today_submissions": today_submissions,
        "this_month_submissions": this_month_submissions,
        "unique_employees": unique_employees,
        "forms_with_submissions": forms_with_submissions,
        "submissions_by_form": form_statistics
    }
