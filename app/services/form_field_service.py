from sqlalchemy.orm import Session

from app.repositories.form_field_repository import FormFieldRepository
from app.schemas.form_field import (
    FormFieldCreate,
    FormFieldUpdate
)


class FormFieldService:

    def __init__(self):
        self.repository = FormFieldRepository()

    def create(
        self,
        db: Session,
        form_id: int,
        data: FormFieldCreate
    ):
        return self.repository.create(
            db,
            form_id,
            data
        )

    def update(
        self,
        db: Session,
        form_id: int,
        field_id: int,
        data: FormFieldUpdate
    ):
        field = self.repository.get_by_id(
            db,
            form_id,
            field_id
        )

        if not field:
            raise ValueError("Form field not found")

        return self.repository.update(
            db,
            field,
            data
        )

    def delete(
        self,
        db: Session,
        form_id: int,
        field_id: int
    ):
        field = self.repository.get_by_id(
            db,
            form_id,
            field_id
        )

        if not field:
            raise ValueError("Form field not found")

        self.repository.delete(db, field)

        return {
            "message": "Form field deleted successfully"
        }