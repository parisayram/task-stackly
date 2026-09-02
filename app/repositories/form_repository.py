from sqlalchemy.orm import Session

from app.models.form import Form
from app.schemas.form import FormCreate, FormUpdate


def create_form(db: Session, form_data: FormCreate):
    form = Form(
        name=form_data.name,
        description=form_data.description,
        created_by=form_data.created_by,
        status=form_data.status
    )

    db.add(form)
    db.commit()
    db.refresh(form)

    return form


def get_forms(db: Session):
    return db.query(Form).all()


def get_form(db: Session, form_id: int):
    return db.query(Form).filter(Form.form_id == form_id).first()


def update_form(db: Session, form_id: int, form_data: FormUpdate):
    form = db.query(Form).filter(Form.form_id == form_id).first()

    if not form:
        return None

    update_data = form_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(form, key, value)

    db.commit()
    db.refresh(form)

    return form


def delete_form(db: Session, form_id: int):
    form = db.query(Form).filter(Form.form_id == form_id).first()

    if not form:
        return None

    db.delete(form)
    db.commit()

    return form
