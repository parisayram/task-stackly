from fastapi import FastAPI

from .database import Base
from .database import engine

from . import models

from .routers.dashboard import router as dashboard_router


# CREATE DATABASE TABLES

Base.metadata.create_all(
    bind=engine
)



# CREATE FASTAPI APP

app = FastAPI(
    title="Form Management & Dashboard API",
    description=(
        "Dashboard Filters and Date Range API"
    ),
    version="1.0.0"
)


# REGISTER DASHBOARD ROUTER

app.include_router(
    dashboard_router
)


# ROOT API

@app.get("/")
def root():

    return {
        "message":
            "Form Management & Dashboard API is running"
    }