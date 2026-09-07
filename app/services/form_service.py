from sqlalchemy.orm import Session

from app.repositories.form_repository import FormRepository
from app.schemas.form import FormCreate, FormUpdate


class FormService:

    def __init__(self):
        self.repository = FormRepository()

    def create(self, db: Session, data: FormCreate):
        return self.repository.create(db, data)

    def get_all(self, db: Session):
        return self.repository.get_all(db)

    def get_by_id(self, db: Session, form_id: int):
        form = self.repository.get_by_id(db, form_id)

        if not form:
            raise ValueError("Form not found")

        return form

    def update(
        self,
        db: Session,
        form_id: int,
        data: FormUpdate
    ):
        form = self.get_by_id(db, form_id)

        return self.repository.update(
            db,
            form,
            data
        )

    def delete(self, db: Session, form_id: int):
        form = self.get_by_id(db, form_id)

        self.repository.delete(db, form)

        return {
            "message": "Form deleted successfully"
        }
