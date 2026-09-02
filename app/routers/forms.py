from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.form import FormCreate, FormUpdate, FormResponse
from app.services import form_service


router = APIRouter(
    prefix="/forms",
    tags=["Forms"]
)


@router.post("/", response_model=FormResponse)
def create_form(
    form_data: FormCreate,
    db: Session = Depends(get_db)
):
    return form_service.create_form(db, form_data)


@router.get("/", response_model=list[FormResponse])
def get_forms(
    db: Session = Depends(get_db)
):
    return form_service.get_forms(db)


@router.get("/{form_id}", response_model=FormResponse)
def get_form(
    form_id: int,
    db: Session = Depends(get_db)
):
    form = form_service.get_form(db, form_id)

    if not form:
        raise HTTPException(
            status_code=404,
            detail="Form not found"
        )

    return form


@router.put("/{form_id}", response_model=FormResponse)
def update_form(
    form_id: int,
    form_data: FormUpdate,
    db: Session = Depends(get_db)
):
    form = form_service.update_form(db, form_id, form_data)

    if not form:
        raise HTTPException(
            status_code=404,
            detail="Form not found"
        )

    return form


@router.delete("/{form_id}")
def delete_form(
    form_id: int,
    db: Session = Depends(get_db)
):
    form = form_service.delete_form(db, form_id)

    if not form:
        raise HTTPException(
            status_code=404,
            detail="Form not found"
        )

    return {
        "message": "Form deleted successfully"
    }
