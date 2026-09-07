from sqlalchemy.orm import Session

from app.repositories.dashboard import get_form_statistics


def fetch_form_statistics(db: Session):
    return get_form_statistics(db)