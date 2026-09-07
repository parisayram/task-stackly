from sqlalchemy.orm import Session

from app.models.form_permission import FormPermission


def create_permission(db: Session, permission: FormPermission):
    db.add(permission)
    db.commit()
    db.refresh(permission)
    return permission


def get_permissions(db: Session, form_id: int):
    return (
        db.query(FormPermission)
        .filter(FormPermission.form_id == form_id)
        .all()
    )


def get_permission(
    db: Session,
    form_id: int,
    permission_id: int
):
    return (
        db.query(FormPermission)
        .filter(
            FormPermission.id == permission_id,
            FormPermission.form_id == form_id
        )
        .first()
    )


def update_permission(
    db: Session,
    permission: FormPermission
):
    db.commit()
    db.refresh(permission)
    return permission


def delete_permission(
    db: Session,
    permission: FormPermission
):
    db.delete(permission)
    db.commit()