from sqlalchemy.orm import Session

from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate
)


class EmployeeService:

    def __init__(self):
        self.repository = EmployeeRepository()

    def create(
        self,
        db: Session,
        data: EmployeeCreate
    ):
        existing_employee = (
            self.repository.get_by_email(
                db,
                data.email
            )
        )

        if existing_employee:
            raise ValueError(
                "Employee with this email already exists"
            )

        if data.status not in {"active", "inactive"}:
            raise ValueError(
                "Status must be either active or inactive"
            )

        return self.repository.create(
            db,
            data
        )

    def get_all(
        self,
        db: Session
    ):
        return self.repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        employee_id: int
    ):
        employee = (
            self.repository.get_by_id(
                db,
                employee_id
            )
        )

        if not employee:
            raise ValueError(
                "Employee not found"
            )

        return employee

    def update(
        self,
        db: Session,
        employee_id: int,
        data: EmployeeUpdate
    ):
        employee = self.get_by_id(
            db,
            employee_id
        )

        if data.email:
            existing_employee = (
                self.repository.get_by_email(
                    db,
                    data.email
                )
            )

            if (
                existing_employee
                and existing_employee.employee_id
                != employee_id
            ):
                raise ValueError(
                    "Employee with this email already exists"
                )

        if (
            data.status is not None
            and data.status not in {"active", "inactive"}
        ):
            raise ValueError(
                "Status must be either active or inactive"
            )

        return self.repository.update(
            db,
            employee,
            data
        )

    def delete(
        self,
        db: Session,
        employee_id: int
    ):
        employee = self.get_by_id(
            db,
            employee_id
        )

        self.repository.delete(
            db,
            employee
        )

        return {
            "message": "Employee deleted successfully"
        }
    