"""
Service layer = business logic + orchestration. Routers call services,
services call repositories. Put your "rules" here, not in the router.
"""
from typing import Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import form_repository
from app.schemas.form import FormCreate, FormUpdate


def create_form(db: Session, data: FormCreate, created_by: Optional[int] = None):
    return form_repository.create_form(db, data, created_by)


def get_form_or_404(db: Session, form_id: int):
    form = form_repository.get_form(db, form_id)
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    return form


def list_forms(db: Session, skip: int = 0, limit: int = 100):
    return form_repository.list_forms(db, skip, limit)


def update_form(db: Session, form_id: int, data: FormUpdate):
    form = get_form_or_404(db, form_id)
    return form_repository.update_form(db, form, data)


def delete_form(db: Session, form_id: int):
    form = get_form_or_404(db, form_id)
    form_repository.delete_form(db, form)
