"""
Repository layer = ONLY database queries. No business logic here —
that belongs in services/. Keeps DB access swappable/testable.
"""
from typing import Optional
from sqlalchemy.orm import Session

from app.models.form import Form
from app.schemas.form import FormCreate, FormUpdate


def create_form(db: Session, data: FormCreate, created_by: Optional[int] = None) -> Form:
    form = Form(**data.model_dump(), created_by=created_by)
    db.add(form)
    db.commit()
    db.refresh(form)
    return form


def get_form(db: Session, form_id: int) -> Optional[Form]:
    return db.query(Form).filter(Form.id == form_id).first()


def list_forms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Form).offset(skip).limit(limit).all()


def update_form(db: Session, form: Form, data: FormUpdate) -> Form:
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(form, key, value)
    db.commit()
    db.refresh(form)
    return form


def delete_form(db: Session, form: Form) -> None:
    db.delete(form)
    db.commit()
