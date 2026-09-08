"""
Entry point. Run with:  uvicorn app.main:app --reload
Everyone runs off this ONE app instance — never create a second
FastAPI() somewhere else.
"""
from fastapi import FastAPI

from app.database import engine, Base
from app import models  # noqa: F401  (registers all tables on Base)
from app.routers import forms, dashboard

# Creates tables that don't exist yet. Fine for dev; use Alembic
# migrations instead once this goes anywhere near production.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Backend Team API",
    description="Forms + Dashboard modules — 14-person backend team",
    version="0.1.0",
)

app.include_router(forms.router)
app.include_router(dashboard.router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
