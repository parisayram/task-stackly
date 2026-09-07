from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.dashboard.dashboard_repository import DashboardRepository
from app.services.dashboard.summary_service import DashboardSummaryService
from app.schemas.dashboard.summary import DashboardSummary


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary", response_model=DashboardSummary)
def get_dashboard_summary(db: Session = Depends(get_db)):
    repository = DashboardRepository(db)
    service = DashboardSummaryService(repository)

    return service.get_summary()