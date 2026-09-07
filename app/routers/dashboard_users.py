from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.dashboard_users import UserStatisticsResponse
from app.services.dashboard_users import DashboardUserService


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard - User Statistics"]
)


@router.get(
    "/users",
    response_model=UserStatisticsResponse,
)
def get_user_statistics(
    db: Session = Depends(get_db),
):
    """
    Get statistics about users in the employee
    management system.
    """

    return DashboardUserService.get_user_statistics(db)