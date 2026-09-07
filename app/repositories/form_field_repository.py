from sqlalchemy.orm import Session

from app.models.form_field import FormField
from app.schemas.form_field import (
    FormFieldCreate,
    FormFieldUpdate
)


class FormFieldRepository:

    def create(
        self,
        db: Session,
        form_id: int,
        data: FormFieldCreate
    ):
        field = FormField(
            form_id=form_id,
            **data.model_dump()
        )

        db.add(field)
        db.commit()
        db.refresh(field)

        return field

    def get_by_id(
        self,
        db: Session,
        form_id: int,
        field_id: int
    ):
        return (
            db.query(FormField)
            .filter(
                FormField.id == field_id,
                FormField.form_id == form_id
            )
            .first()
        )

    def update(
        self,
        db: Session,
        field: FormField,
        data: FormFieldUpdate
    ):
        values = data.model_dump(
            exclude_unset=True
        )

        for key, value in values.items():
            setattr(field, key, value)

        db.commit()
        db.refresh(field)

        return field

    def delete(
        self,
        db: Session,
        field: FormField
    ):
        db.delete(field)
        db.commit()