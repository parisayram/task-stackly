from sqlalchemy.orm import Session

from app.models.form import Form
from app.schemas.form import FormCreate, FormUpdate


class FormRepository:

    def create(self, db: Session, data: FormCreate):
        form = Form(**data.model_dump())

        db.add(form)
        db.commit()
        db.refresh(form)

        return form

    def get_all(self, db: Session):
        return db.query(Form).all()

    def get_by_id(self, db: Session, form_id: int):
        return (
            db.query(Form)
            .filter(Form.id == form_id)
            .first()
        )

    def update(
        self,
        db: Session,
        form: Form,
        data: FormUpdate
    ):
        values = data.model_dump(exclude_unset=True)

        for key, value in values.items():
            setattr(form, key, value)

        db.commit()
        db.refresh(form)

        return form

    def delete(self, db: Session, form: Form):
        db.delete(form)
        db.commit()

