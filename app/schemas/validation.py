from typing import Any

from pydantic import BaseModel


class FormValidationRequest(BaseModel):
    data: dict[str, Any]


class FormValidationResponse(BaseModel):
    valid: bool
    errors: list[str]