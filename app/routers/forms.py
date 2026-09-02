from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.form import (
    FormCreate,
    FormUpdate,
    FormResponse
)

from app.services.form_service import FormService


router = APIRouter(
    prefix="/forms",
    tags=["Forms"]
)

service = FormService()


@router.post("/", response_model=FormResponse)
def create_form(
    data: FormCreate,
    db: Session = Depends(get_db)
):
    return service.create(db, data)


@router.get("/", response_model=list[FormResponse])
def get_forms(
    db: Session = Depends(get_db)
):
    return service.get_all(db)


@router.get("/{form_id}", response_model=FormResponse)
def get_form(
    form_id: int,
    db: Session = Depends(get_db)
):
    try:
        return service.get_by_id(db, form_id)
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.put("/{form_id}", response_model=FormResponse)
def update_form(
    form_id: int,
    data: FormUpdate,
    db: Session = Depends(get_db)
):
    try:
        return service.update(
            db,
            form_id,
            data
        )
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete("/{form_id}")
def delete_form(
    form_id: int,
    db: Session = Depends(get_db)
):
    try:
        return service.delete(
            db,
            form_id
        )
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
