from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.dashboard import FormStatisticsResponse
from app.services.dashboard import fetch_form_statistics


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/forms",
    response_model=FormStatisticsResponse
)
def get_form_statistics(db: Session = Depends(get_db)):
    return fetch_form_statistics(db)