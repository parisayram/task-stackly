from typing import Optional
from sqlalchemy.orm import Session

from app.models.field import FormField
from app.schemas.field import FieldCreate, FieldUpdate


def create_field(db: Session, form_id: int, data: FieldCreate) -> FormField:
    field = FormField(**data.model_dump(), form_id=form_id)
    db.add(field)
    db.commit()
    db.refresh(field)
    return field


def get_field(db: Session, form_id: int, field_id: int) -> Optional[FormField]:
    return db.query(FormField).filter(
        FormField.id == field_id, FormField.form_id == form_id
    ).first()


def list_fields(db: Session, form_id: int):
    return (
        db.query(FormField)
        .filter(FormField.form_id == form_id)
        .order_by(FormField.order)
        .all()
    )


def update_field(db: Session, field: FormField, data: FieldUpdate) -> FormField:
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(field, key, value)
    db.commit()
    db.refresh(field)
    return field


def delete_field(db: Session, field: FormField) -> None:
    db.delete(field)
    db.commit()
