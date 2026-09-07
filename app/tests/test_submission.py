from unittest.mock import MagicMock, patch

import pytest

from app.schemas.submission import SubmissionCreate
from app.services.submission_service import (
    create_submission,
    get_submission,
)


def test_create_submission_success():
    db = MagicMock()

    form = MagicMock()
    employee = MagicMock()

    # First query checks Form
    form_query = MagicMock()
    form_query.filter.return_value.first.return_value = form

    # Second query checks Employee
    employee_query = MagicMock()
    employee_query.filter.return_value.first.return_value = employee

    db.query.side_effect = [form_query, employee_query]

    submission = SubmissionCreate(
        form_id=1,
        employee_id=1,
        data={
            "name": "John",
            "department": "IT"
        }
    )

    expected_result = MagicMock()

    with patch(
        "app.services.submission_service.submission_repository.create_submission",
        return_value=expected_result
    ) as mock_create:

        result = create_submission(db, submission)

    assert result == expected_result
    mock_create.assert_called_once()


def test_create_submission_form_not_found():
    db = MagicMock()

    form_query = MagicMock()
    form_query.filter.return_value.first.return_value = None

    db.query.return_value = form_query

    submission = SubmissionCreate(
        form_id=999,
        employee_id=1,
        data={
            "name": "John"
        }
    )

    with pytest.raises(ValueError, match="Form not found"):
        create_submission(db, submission)


def test_create_submission_employee_not_found():
    db = MagicMock()

    form = MagicMock()

    form_query = MagicMock()
    form_query.filter.return_value.first.return_value = form

    employee_query = MagicMock()
    employee_query.filter.return_value.first.return_value = None

    db.query.side_effect = [form_query, employee_query]

    submission = SubmissionCreate(
        form_id=1,
        employee_id=999,
        data={
            "name": "John"
        }
    )

    with pytest.raises(ValueError, match="Employee not found"):
        create_submission(db, submission)


def test_get_submission_success():
    db = MagicMock()

    expected_submission = MagicMock()

    with patch(
        "app.services.submission_service.submission_repository.get_submission",
        return_value=expected_submission
    ):

        result = get_submission(db, 1)

    assert result == expected_submission


def test_get_submission_not_found():
    db = MagicMock()

    with patch(
        "app.services.submission_service.submission_repository.get_submission",
        return_value=None
    ):

        with pytest.raises(ValueError, match="Submission not found"):
            get_submission(db, 999)