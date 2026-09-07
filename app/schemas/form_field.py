from pydantic import BaseModel


class FormFieldCreate(BaseModel):
    field_name: str
    field_type: str
    label: str
    placeholder: str | None = None
    is_required: bool = False
    options: str | None = None


class FormFieldUpdate(BaseModel):
    field_name: str | None = None
    field_type: str | None = None
    label: str | None = None
    placeholder: str | None = None
    is_required: bool | None = None
    options: str | None = None


class FormFieldResponse(FormFieldCreate):
    id: int
    form_id: int

    class Config:
        from_attributes = True