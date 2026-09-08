"""Owner: Naganaboina Sumanth (Form Validation APIs)."""
import re
from typing import Any, Dict
from sqlalchemy.orm import Session

from app.repositories import field_repository
from app.schemas.submission import ValidationError, ValidationResult


def validate_submission(db: Session, form_id: int, data: Dict[str, Any]) -> ValidationResult:
    fields = field_repository.list_fields(db, form_id)
    errors = []

    for field in fields:
        value = data.get(str(field.id))

        if field.is_required and (value is None or value == ""):
            errors.append(ValidationError(field_id=field.id, message=f"'{field.label}' is required"))
            continue

        if value is None:
            continue

        rules = field.validation_rules or {}

        if field.field_type == "number":
            if not isinstance(value, (int, float)):
                errors.append(ValidationError(field_id=field.id, message=f"'{field.label}' must be a number"))
                continue
            if "min" in rules and value < rules["min"]:
                errors.append(ValidationError(field_id=field.id, message=f"'{field.label}' below minimum"))
            if "max" in rules and value > rules["max"]:
                errors.append(ValidationError(field_id=field.id, message=f"'{field.label}' above maximum"))

        if field.field_type == "text" and "regex" in rules:
            if not re.match(rules["regex"], str(value)):
                errors.append(ValidationError(field_id=field.id, message=f"'{field.label}' has invalid format"))

        if field.field_type in ("select", "radio") and field.options:
            if value not in field.options:
                errors.append(ValidationError(field_id=field.id, message=f"'{field.label}' has invalid option"))

    return ValidationResult(valid=len(errors) == 0, errors=errors)
