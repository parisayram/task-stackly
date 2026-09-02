from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.form_field import (
    FormFieldCreate,
    FormFieldUpdate,
    FormFieldResponse
)

from app.services.form_field_service import FormFieldService


router = APIRouter(
    prefix="/forms",
    tags=["Form Fields"]
)

service = FormFieldService()


@router.post(
    "/{form_id}/fields",
    response_model=FormFieldResponse
)
def create_field(
    form_id: int,
    data: FormFieldCreate,
    db: Session = Depends(get_db)
):
    return service.create(
        db,
        form_id,
        data
    )


@router.put(
    "/{form_id}/fields/{field_id}",
    response_model=FormFieldResponse
)
def update_field(
    form_id: int,
    field_id: int,
    data: FormFieldUpdate,
    db: Session = Depends(get_db)
):
    try:
        return service.update(
            db,
            form_id,
            field_id,
            data
        )
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete(
    "/{form_id}/fields/{field_id}"
)
def delete_field(
    form_id: int,
    field_id: int,
    db: Session = Depends(get_db)
):
    try:
        return service.delete(
            db,
            form_id,
            field_id
        )
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )