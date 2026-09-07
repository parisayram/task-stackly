from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from ..models import Submission


def get_dashboard_filters(
    db: Session,
    form_id: Optional[int] = None,
    status: Optional[str] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
    page: int = 1,
    page_size: int = 10
):

    query = db.query(Submission)


    # FILTER BY FORM ID
   
    if form_id is not None:

        query = query.filter(
            Submission.form_id == form_id
        )


    # FILTER BY STATUS

    if status is not None:

        query = query.filter(
            Submission.status == status
        )


    # FILTER BY FROM DATE

    if from_date is not None:

        query = query.filter(
            Submission.submitted_at >= from_date
        )

 
    # FILTER BY TO DATE

    if to_date is not None:

        query = query.filter(
            Submission.submitted_at <= to_date
        )


    # TOTAL RECORDS

    total_submissions = query.count()


    # STATUS COUNTS

    pending_submissions = query.filter(
        Submission.status == "pending"
    ).count()

    approved_submissions = query.filter(
        Submission.status == "approved"
    ).count()

    rejected_submissions = query.filter(
        Submission.status == "rejected"
    ).count()


    # PAGINATION

    offset = (page - 1) * page_size

    submissions = (
        query
        .order_by(
            Submission.submitted_at.desc()
        )
        .offset(offset)
        .limit(page_size)
        .all()
    )


    # TOTAL PAGES

    total_pages = (
        total_submissions + page_size - 1
    ) // page_size


    # RETURN RESULT

    return {
        "total_submissions": total_submissions,

        "pending_submissions":
            pending_submissions,

        "approved_submissions":
            approved_submissions,

        "rejected_submissions":
            rejected_submissions,

        "from_date": from_date,

        "to_date": to_date,

        "page": page,

        "page_size": page_size,

        "total_pages": total_pages,

        "submissions": submissions
    }