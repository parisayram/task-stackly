from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    department: str | None = None
    designation: str | None = None
    status: str = "active"


class EmployeeUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    department: str | None = None
    designation: str | None = None
    status: str | None = None


class EmployeeResponse(BaseModel):
    employee_id: int
    name: str
    email: EmailStr
    department: str | None = None
    designation: str | None = None
    status: str
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
    