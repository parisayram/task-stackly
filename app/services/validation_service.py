from sqlalchemy.orm import Session

from app.models.form_field import FormField


def validate_form(
    db: Session,
    form_id: int,
    data: dict
):
    fields = (
        db.query(FormField)
        .filter(FormField.form_id == form_id)
        .all()
    )

    errors = []

    for field in fields:

        value = data.get(field.field_name)

        if field.is_required:
            if value is None or value == "":
                errors.append(
                    f"{field.label} is required"
                )
                continue

        if value is None:
            continue

        if field.field_type == "email":
            if "@" not in str(value):
                errors.append(
                    f"{field.label} must be a valid email"
                )

        elif field.field_type == "number":
            try:
                float(value)
            except (ValueError, TypeError):
                errors.append(
                    f"{field.label} must be a number"
                )

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }