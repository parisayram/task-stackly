from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models.employee import Employee
from app.models.form import Form
from app.models.submission import Submission
from app.services.dashboard_activity import fetch_recent_activity


def test_fetch_recent_activity_returns_latest_submissions_with_context():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    session = sessionmaker(bind=engine)()

    form = Form(name="Employee Registration", description="Employee details")
    employee = Employee(name="Asha Kumar", email="asha@example.com")
    session.add_all([form, employee])
    session.flush()

    first_time = datetime(2026, 9, 1, 9, 0)
    second_time = first_time + timedelta(hours=1)
    session.add_all([
        Submission(
            form_id=form.id,
            employee_id=employee.employee_id,
            data="{}",
            submitted_at=first_time,
        ),
        Submission(
            form_id=form.id,
            employee_id=employee.employee_id,
            data="{}",
            submitted_at=second_time,
        ),
    ])
    session.commit()

    response = fetch_recent_activity(session, limit=1)

    assert len(response["activities"]) == 1
    activity = response["activities"][0]
    assert activity["activity_type"] == "submission"
    assert activity["form_name"] == "Employee Registration"
    assert activity["employee_name"] == "Asha Kumar"
    assert activity["occurred_at"] == second_time

    session.close()