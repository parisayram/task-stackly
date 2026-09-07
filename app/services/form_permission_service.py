from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.form_permission import FormPermission
from app.schemas.form_permission import (
    FormPermissionCreate,
    FormPermissionUpdate,
)
from app.repositories import form_permission_repository


def create_permission(
    db: Session,
    data: FormPermissionCreate
):
    permission = FormPermission(**data.model_dump())

    return form_permission_repository.create_permission(
        db,
        permission
    )


def get_permissions(
    db: Session,
    form_id: int
):
    return form_permission_repository.get_permissions(
        db,
        form_id
    )


def update_permission(
    db: Session,
    form_id: int,
    permission_id: int,
    data: FormPermissionUpdate
):
    permission = form_permission_repository.get_permission(
        db,
        form_id,
        permission_id
    )

    if not permission:
        raise HTTPException(
            status_code=404,
            detail="Permission not found"
        )

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(permission, key, value)

    return form_permission_repository.update_permission(
        db,
        permission
    )


def delete_permission(
    db: Session,
    form_id: int,
    permission_id: int
):
    permission = form_permission_repository.get_permission(
        db,
        form_id,
        permission_id
    )

    if not permission:
        raise HTTPException(
            status_code=404,
            detail="Permission not found"
        )

    form_permission_repository.delete_permission(
        db,
        permission
    )

    return {"message": "Permission deleted successfully"}