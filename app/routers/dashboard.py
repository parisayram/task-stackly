from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query

from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import DashboardFilterResponse
from ..services.dashboard_service import get_dashboard_filters


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/filters",
    response_model=DashboardFilterResponse
)
def dashboard_filters(

    form_id: Optional[int] = Query(
        default=None,
        description="Filter submissions by Form ID"
    ),

    status: Optional[str] = Query(
        default=None,
        description="Filter by submission status"
    ),

    from_date: Optional[datetime] = Query(
        default=None,
        description="Start date and time"
    ),

    to_date: Optional[datetime] = Query(
        default=None,
        description="End date and time"
    ),

    page: int = Query(
        default=1,
        ge=1,
        description="Page number"
    ),

    page_size: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Number of records per page"
    ),

    db: Session = Depends(get_db)
):


    # DATE VALIDATION

    if from_date and to_date:

        if from_date > to_date:

            raise HTTPException(
                status_code=400,
                detail=(
                    "from_date cannot be greater "
                    "than to_date"
                )
            )


    # STATUS VALIDATION

    allowed_statuses = [
        "pending",
        "approved",
        "rejected"
    ]

    if status is not None:

        status = status.lower()

        if status not in allowed_statuses:

            raise HTTPException(
                status_code=400,
                detail=(
                    "Invalid status. Allowed values: "
                    "pending, approved, rejected"
                )
            )


    # SERVICE CALL

    result = get_dashboard_filters(

        db=db,

        form_id=form_id,

        status=status,

        from_date=from_date,

        to_date=to_date,

        page=page,

        page_size=page_size
    )

    return result