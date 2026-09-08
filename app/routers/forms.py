"""
Forms Group router — all 7 people's endpoints live in this ONE router
file (same prefix), but each function calls into ITS OWN service file.
Do not edit someone else's function; add yours in the matching section.

IMPORTANT: static paths like /forms/search MUST be declared before
dynamic paths like /forms/{form_id}, or FastAPI will try to parse
"search" as form_id and throw a 422.
"""
from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.form import FormCreate, FormUpdate, FormOut
from app.schemas.field import FieldCreate, FieldUpdate, FieldOut
from app.schemas.submission import SubmissionCreate, SubmissionOut, ValidationResult, StatusUpdate, StatusHistoryOut
from app.services import (
    form_service, field_service, validation_service,
    submission_service, search_service, permission_service,
)

router = APIRouter(prefix="/forms", tags=["Forms"])


# ---- Surisetty Kamesh: Form Search, Filter & Pagination ----
# Declared first because it's a static path ("/forms/search").
@router.get("/search")
def search_forms(
    q: Optional[str] = None,
    is_active: Optional[bool] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return search_service.search_forms(db, q, is_active, page, page_size)


# ---- Kallam Poojitha: Form CRUD APIs ----
@router.post("", response_model=FormOut, status_code=201)
def create_form(payload: FormCreate, db: Session = Depends(get_db)):
    return form_service.create_form(db, payload)


@router.get("", response_model=list[FormOut])
def list_forms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return form_service.list_forms(db, skip, limit)


@router.get("/{form_id}", response_model=FormOut)
def get_form(form_id: int, db: Session = Depends(get_db)):
    return form_service.get_form_or_404(db, form_id)


@router.put("/{form_id}", response_model=FormOut)
def update_form(form_id: int, payload: FormUpdate, db: Session = Depends(get_db)):
    return form_service.update_form(db, form_id, payload)


@router.delete("/{form_id}", status_code=204)
def delete_form(form_id: int, db: Session = Depends(get_db)):
    form_service.delete_form(db, form_id)


# ---- Kadirimangalam: Form Fields APIs ----
@router.post("/{form_id}/fields", response_model=FieldOut, status_code=201)
def add_field(form_id: int, payload: FieldCreate, db: Session = Depends(get_db)):
    return field_service.create_field(db, form_id, payload)


@router.get("/{form_id}/fields", response_model=list[FieldOut])
def get_fields(form_id: int, db: Session = Depends(get_db)):
    return field_service.list_fields(db, form_id)


@router.put("/{form_id}/fields/{field_id}", response_model=FieldOut)
def update_field(form_id: int, field_id: int, payload: FieldUpdate, db: Session = Depends(get_db)):
    return field_service.update_field(db, form_id, field_id, payload)


@router.delete("/{form_id}/fields/{field_id}", status_code=204)
def delete_field(form_id: int, field_id: int, db: Session = Depends(get_db)):
    field_service.delete_field(db, form_id, field_id)


# ---- Naganaboina Sumanth: Form Validation APIs ----
@router.post("/{form_id}/validate", response_model=ValidationResult)
def validate_form_data(form_id: int, payload: dict, db: Session = Depends(get_db)):
    return validation_service.validate_submission(db, form_id, payload)


# ---- Sheetal: Form Submission APIs ----
@router.post("/{form_id}/submit", response_model=SubmissionOut, status_code=201)
def submit_form(form_id: int, payload: SubmissionCreate, db: Session = Depends(get_db)):
    return submission_service.create_submission(db, form_id, payload)


# ---- Sumanth M T: Submission History & Status APIs ----
@router.get("/{form_id}/submissions", response_model=list[SubmissionOut])
def get_submissions(form_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return submission_service.list_submissions(db, form_id, skip, limit)


@router.get("/{form_id}/submissions/{submission_id}", response_model=SubmissionOut)
def get_submission(form_id: int, submission_id: int, db: Session = Depends(get_db)):
    return submission_service.get_submission_or_404(db, form_id, submission_id)


@router.put("/{form_id}/submissions/{submission_id}/status", response_model=SubmissionOut)
def update_submission_status(form_id: int, submission_id: int, payload: StatusUpdate, db: Session = Depends(get_db)):
    return submission_service.update_status(db, form_id, submission_id, payload)


@router.get("/{form_id}/submissions/{submission_id}/history", response_model=list[StatusHistoryOut])
def get_submission_history(form_id: int, submission_id: int, db: Session = Depends(get_db)):
    return submission_service.get_history(db, form_id, submission_id)


# ---- Addhuru Poojitha: Form Permissions & Access Control ----
@router.post("/{form_id}/permissions")
def grant_permission(form_id: int, user_id: int, role: str = "viewer", db: Session = Depends(get_db)):
    return permission_service.grant_permission(db, form_id, user_id, role)


@router.get("/{form_id}/permissions")
def list_permissions(form_id: int, db: Session = Depends(get_db)):
    return permission_service.list_permissions(db, form_id)
