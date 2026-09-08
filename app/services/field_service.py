from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import field_repository
from app.services.form_service import get_form_or_404
from app.schemas.field import FieldCreate, FieldUpdate


def create_field(db: Session, form_id: int, data: FieldCreate):
    get_form_or_404(db, form_id)  # 404 if form doesn't exist
    return field_repository.create_field(db, form_id, data)


def get_field_or_404(db: Session, form_id: int, field_id: int):
    field = field_repository.get_field(db, form_id, field_id)
    if not field:
        raise HTTPException(status_code=404, detail="Field not found")
    return field


def list_fields(db: Session, form_id: int):
    get_form_or_404(db, form_id)
    return field_repository.list_fields(db, form_id)


def update_field(db: Session, form_id: int, field_id: int, data: FieldUpdate):
    field = get_field_or_404(db, form_id, field_id)
    return field_repository.update_field(db, field, data)


def delete_field(db: Session, form_id: int, field_id: int):
    field = get_field_or_404(db, form_id, field_id)
    field_repository.delete_field(db, field)
