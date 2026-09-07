from pydantic import BaseModel, ConfigDict


class FormPermissionCreate(BaseModel):
    form_id: int
    employee_id: int
    can_view: bool = True
    can_submit: bool = False
    can_edit: bool = False
    can_delete: bool = False


class FormPermissionUpdate(BaseModel):
    can_view: bool | None = None
    can_submit: bool | None = None
    can_edit: bool | None = None
    can_delete: bool | None = None


class FormPermissionResponse(BaseModel):
    id: int
    form_id: int
    employee_id: int
    can_view: bool
    can_submit: bool
    can_edit: bool
    can_delete: bool

    model_config = ConfigDict(from_attributes=True)