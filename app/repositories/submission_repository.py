from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.form import Form
from app.models.submission import Submission


def get_submission_analytics(db: Session):
    total_submissions = (
        db.query(func.count(Submission.id))
        .scalar()
        or 0
    )

    unique_forms = (
        db.query(
            func.count(
                func.distinct(Submission.form_id)
            )
        )
        .scalar()
        or 0
    )

    unique_employees = (
        db.query(
            func.count(
                func.distinct(Submission.employee_id)
            )
        )
        .scalar()
        or 0
    )

    submission_statistics = (
        db.query(
            Form.id.label("form_id"),
            Form.name.label("form_name"),
            func.count(Submission.id).label(
                "submission_count"
            )
        )
        .join(
            Submission,
            Submission.form_id == Form.id
        )
        .group_by(
            Form.id,
            Form.name
        )
        .order_by(
            func.count(Submission.id).desc()
        )
        .all()
    )

    return {
        "total_submissions": total_submissions,
        "unique_forms": unique_forms,
        "unique_employees": unique_employees,
        "submissions": [
            {
                "form_id": row.form_id,
                "form_name": row.form_name,
                "submission_count": row.submission_count,
            }
            for row in submission_statistics
        ],
    }
