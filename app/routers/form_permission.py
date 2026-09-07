from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.form_permission import (
    FormPermissionCreate,
    FormPermissionUpdate,
    FormPermissionResponse,
)
from app.services import form_permission_service


router = APIRouter(
    prefix="/forms",
    tags=["Form Permissions"]
)


@router.post(
    "/{form_id}/permissions",
    response_model=FormPermissionResponse,
    status_code=status.HTTP_201_CREATED
)
def create_permission(
    form_id: int,
    data: FormPermissionCreate,
    db: Session = Depends(get_db)
):
    if data.form_id != form_id:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=400,
            detail="form_id in body must match URL form_id"
        )

    return form_permission_service.create_permission(
        db,
        data
    )


@router.get(
    "/{form_id}/permissions",
    response_model=list[FormPermissionResponse]
)
def get_permissions(
    form_id: int,
    db: Session = Depends(get_db)
):
    return form_permission_service.get_permissions(
        db,
        form_id
    )


@router.put(
    "/{form_id}/permissions/{permission_id}",
    response_model=FormPermissionResponse
)
def update_permission(
    form_id: int,
    permission_id: int,
    data: FormPermissionUpdate,
    db: Session = Depends(get_db)
):
    return form_permission_service.update_permission(
        db,
        form_id,
        permission_id,
        data
    )


@router.delete(
    "/{form_id}/permissions/{permission_id}"
)
def delete_permission(
    form_id: int,
    permission_id: int,
    db: Session = Depends(get_db)
):
    return form_permission_service.delete_permission(
        db,
        form_id,
        permission_id
    )