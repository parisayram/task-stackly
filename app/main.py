from fastapi import FastAPI

from .database import Base, engine

# Import models so SQLAlchemy can create all tables
from .models.form import Form
from .models.form_field import FormField
from .models.submission import Submission
from .models.employee import Employee
from .models.form_permission import FormPermission

# Import routers
from .routers.dashboard import router as dashboard_router
from .routers.forms import router as forms_router
from .routers.form_fields import router as form_fields_router
from .routers.validation import router as validation_router
from .routers.submission import router as submission_router
from .routers.employees import router as employees_router
from .routers.form_permission import router as form_permission_router


# CREATE DATABASE TABLES

Base.metadata.create_all(bind=engine)


# CREATE FASTAPI APP

app = FastAPI(
    title="Form Management & Dashboard API",
    description=(
        "Form Management, Dashboard Filters "
        "and Date Range API"
    ),
    version="1.0.0"
)


# REGISTER ROUTERS

app.include_router(forms_router)
app.include_router(form_fields_router)
app.include_router(validation_router)
app.include_router(submission_router)
app.include_router(employees_router)
app.include_router(form_permission_router)

# Dashboard Filters API
app.include_router(dashboard_router)


# ROOT API

@app.get("/")
def root():
    return {
        "message": "Form Management & Dashboard API is running"
    }