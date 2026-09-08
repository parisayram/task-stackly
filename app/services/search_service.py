
from typing import Optional

from sqlalchemy.orm import Session

from app.models.form import Form


def search_forms(
    db: Session,
    search: Optional[str] = None,
    is_active: Optional[bool] = None,
    page: int = 1,
    size: int = 10
):
    """
    Search, filter and paginate forms.

    Parameters:
        db: SQLAlchemy database session
        search: Search text for form title
        is_active: Filter forms by active/inactive status
        page: Page number
        size: Number of records per page

    Returns:
        Dictionary containing pagination information and forms.
    """


    # Validate page
    
    if page < 1:
        page = 1

    # Validate page size
    
    if size < 1:
        size = 10

    # Maximum records per page
    if size > 100:
        size = 100

    
    # Start query
    query = db.query(Form)

    # Search by form title
    if search:
        search = search.strip()

        if search:
            query = query.filter(
                Form.title.ilike(f"%{search}%")
            )

    # -----------------------------
    # Filter by active status
    # -----------------------------
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
        .order_by(Form.id.desc())
        .offset(offset)
        .limit(size)
        .all()
    )

    
    # Calculate total pages
    if total == 0:
        total_pages = 0
    else:
        total_pages = (total + size - 1) // size

    # Return result
    return {
        "page": page,
        "size": size,
        "total": total,
        "pages": total_pages,
        "data": forms
    }
