from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.submission import (
    SubmissionCreate,
    SubmissionResponse
)
from app.services.submission_service import (
    create_submission,
    get_submission,
    get_submissions_by_form,
    get_submissions_by_employee
)


router = APIRouter(
    prefix="/submissions",
    tags=["Submissions"]
)


@router.post("/", response_model=SubmissionResponse)
def create(
    data: SubmissionCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_submission(db, data)
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.get("/form/{form_id}", response_model=list[SubmissionResponse])
def get_by_form(
    form_id: int,
    db: Session = Depends(get_db)
):
    return get_submissions_by_form(db, form_id)


@router.get("/employee/{employee_id}", response_model=list[SubmissionResponse])
def get_by_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return get_submissions_by_employee(db, employee_id)


@router.get("/{submission_id}", response_model=SubmissionResponse)
def get_one(
    submission_id: int,
    db: Session = Depends(get_db)
):
    try:
        return get_submission(db, submission_id)
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )