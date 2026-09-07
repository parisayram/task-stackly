from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.dashboard import SubmissionAnalyticsResponse
from app.services.dashboard_service import get_submission_analytics


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/submissions",
    response_model=SubmissionAnalyticsResponse
)
def submission_analytics(
    db: Session = Depends(get_db)
):
    return get_submission_analytics(db)
