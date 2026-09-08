from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.dashboard_activity import ActivityResponse
from app.services.dashboard_activity import fetch_recent_activity


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard - Recent Activity"],
)


@router.get("/activity", response_model=ActivityResponse)
def get_recent_activity(
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return fetch_recent_activity(db, limit)