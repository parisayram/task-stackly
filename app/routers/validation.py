from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.validation import (
    FormValidationRequest,
    FormValidationResponse
)

from app.services.validation_service import validate_form


router = APIRouter(
    prefix="/forms",
    tags=["Form Validation"]
)


@router.post(
    "/{form_id}/validate",
    response_model=FormValidationResponse
)
def validate(
    form_id: int,
    request: FormValidationRequest,
    db: Session = Depends(get_db)
):
    return validate_form(
        db,
        form_id,
        request.data
    )