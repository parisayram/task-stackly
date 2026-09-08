
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.form import Form
from app.schemas.form import FormResponse
from app.dependencies import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/forms",
    tags=["Form Search"]
)


@router.get("/search")
def search_forms(
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Validate page
    if page < 1:
        page = 1

    # Validate size
    if size < 1:
        size = 10

    # Maximum 100 records per page
    if size > 100:
        size = 100

    # Start query
    query = db.query(Form)

    # Search by title
    if search:
        query = query.filter(
            Form.title.ilike(f"%{search}%")
        )

    # Filter by active status
    if is_active is not None:
        query = query.filter(
            Form.is_active == is_active
        )

    # Total records
    total = query.count()

    # Pagination
    offset = (page - 1) * size

    forms = (
        query
        .offset(offset)
        .limit(size)
        .all()
    )

    # Calculate total pages
    pages = (
        (total + size - 1) // size
        if total > 0
        else 0
    )

    return {
        "page": page,
        "size": size,
        "total": total,
        "pages": pages,
        "data": [
            FormResponse.model_validate(form).model_dump()
            for form in forms
        ]
    }
