from sqlalchemy.orm import Session

from app.repositories.dashboard_activity import get_recent_activity


def fetch_recent_activity(db: Session, limit: int):
    return {"activities": get_recent_activity(db, limit)}