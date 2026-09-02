from fastapi import FastAPI

from app.models.employee import Employee
from app.models.form import Form

from app.routers.forms import router as forms_router


app = FastAPI(
    title="Forms Dashboard API"
)


app.include_router(forms_router)
