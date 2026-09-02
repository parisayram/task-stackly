from sqlalchemy.orm import Session

from app.repositories import form_repository
from app.schemas.form import FormCreate, FormUpdate


def create_form(db: Session, form_data: FormCreate):
    return form_repository.create_form(db, form_data)


def get_forms(db: Session):
    return form_repository.get_forms(db)


def get_form(db: Session, form_id: int):
    return form_repository.get_form(db, form_id)


def update_form(db: Session, form_id: int, form_data: FormUpdate):
    return form_repository.update_form(db, form_id, form_data)


def delete_form(db: Session, form_id: int):
    return form_repository.delete_form(db, form_id)
