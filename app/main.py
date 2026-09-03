from fastapi import FastAPI

from app.database import Base, engine

from app.models.form import Form
from app.models.form_field import FormField
from app.models.submission import Submission

from app.routers.forms import router as forms_router
from app.routers.form_fields import router as form_fields_router
from app.routers.validation import router as validation_router
from app.routers.submission import router as submission_router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Employee Form API",
    description="Employee Form Management System",
    version="1.0.0"
)


# Include routers
app.include_router(forms_router)
app.include_router(form_fields_router)
app.include_router(validation_router)
app.include_router(submission_router)


@app.get("/")
def root():
    return {
        "message": "Employee Form API is running"
    }