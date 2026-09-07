from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


class EmployeeRepository:

    def create(
        self,
        db: Session,
        data: EmployeeCreate
    ):
        employee = Employee(
            **data.model_dump()
        )

        db.add(employee)
        db.commit()
        db.refresh(employee)

        return employee

    def get_all(
        self,
        db: Session
    ):
        return (
            db.query(Employee)
            .order_by(Employee.employee_id)
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        employee_id: int
    ):
        return (
            db.query(Employee)
            .filter(
                Employee.employee_id == employee_id
            )
            .first()
        )

    def get_by_email(
        self,
        db: Session,
        email: str
    ):
        return (
            db.query(Employee)
            .filter(
                Employee.email == email
            )
            .first()
        )

    def update(
        self,
        db: Session,
        employee: Employee,
        data: EmployeeUpdate
    ):
        values = data.model_dump(
            exclude_unset=True
        )

        for key, value in values.items():
            setattr(employee, key, value)

        db.commit()
        db.refresh(employee)

        return employee

    def delete(
        self,
        db: Session,
        employee: Employee
    ):
        db.delete(employee)
        db.commit()