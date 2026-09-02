# Task Stackly

## Overview

Task Stackly is a FastAPI-based application for managing forms,
form fields, submissions, and dashboard information.

## Technology Stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- MySQL
- Pytest

## Project Structure

app/
+-- routers/
+-- models/
+-- schemas/
+-- services/
+-- repositories/
+-- tests/

## Team Modules

### Forms

- Form CRUD APIs
- Form Fields APIs
- Form Validation APIs
- Form Submission APIs
- Submission History & Status APIs
- Form Search, Filter & Pagination
- Form Permissions & Access Control

### Dashboard

- Dashboard Summary API
- User Statistics API
- Form Statistics API
- Submission Analytics API
- Recent Activity API
- Dashboard Filters & Date Range
- Dashboard Export/Report API

## Setup

Create virtual environment:

python -m venv venv

Activate virtual environment:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

## Run Application

python -m uvicorn app.main:app --reload

## API Documentation

Swagger UI:

/docs

ReDoc:

/redoc
