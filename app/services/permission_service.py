"""Owner: Addhuru Poojitha (Form Permissions & Access Control)."""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.permission import FormPermission

ROLE_RANK = {"viewer": 1, "editor": 2, "owner": 3}


def grant_permission(db: Session, form_id: int, user_id: int, role: str = "viewer") -> FormPermission:
    existing = (
        db.query(FormPermission)
        .filter(FormPermission.form_id == form_id, FormPermission.user_id == user_id)
        .first()
    )
    if existing:
        existing.role = role
        db.commit()
        db.refresh(existing)
        return existing

    perm = FormPermission(form_id=form_id, user_id=user_id, role=role)
    db.add(perm)
    db.commit()
    db.refresh(perm)
    return perm


def list_permissions(db: Session, form_id: int):
    return db.query(FormPermission).filter(FormPermission.form_id == form_id).all()


def require_role(db: Session, form_id: int, user_id: int, min_role: str = "viewer"):
    """Call at the top of a protected route: require_role(db, form_id, user_id, 'editor')."""
    perm = (
        db.query(FormPermission)
        .filter(FormPermission.form_id == form_id, FormPermission.user_id == user_id)
        .first()
    )
    if not perm or ROLE_RANK.get(perm.role, 0) < ROLE_RANK.get(min_role, 0):
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    return perm
