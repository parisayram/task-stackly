"""Owner: Surisetty Kamesh (Form Search, Filter & Pagination)."""
from typing import Optional
from sqlalchemy.orm import Session

from app.models.form import Form


def search_forms(
    db: Session,
    q: Optional[str] = None,
    is_active: Optional[bool] = None,
    page: int = 1,
    page_size: int = 20,
):
    query = db.query(Form)

    if q:
        query = query.filter(Form.title.ilike(f"%{q}%"))
    if is_active is not None:
        query = query.filter(Form.is_active == is_active)

    total = query.count()
    items = query.offset((page - 1) * page_size).limit(page_size).all()

    return {
        "items": items,
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": (total + page_size - 1) // page_size,
    }
