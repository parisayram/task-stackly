from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.employee import Employee
from app.models.form import Form
from app.models.submission import Submission


class DashboardRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_total_employees(self):
        return self.db.query(
            func.count(Employee.employee_id)
        ).scalar()

    def get_active_employees(self):
        return (
            self.db.query(func.count(Employee.employee_id))
            .filter(Employee.status == "active")
            .scalar()
        )

    def get_total_forms(self):
        return self.db.query(
            func.count(Form.id)
        ).scalar()

    def get_total_submissions(self):
        return self.db.query(
            func.count(Submission.id)
        ).scalar()