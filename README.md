# Form Management & Dashboard API

A FastAPI backend project for managing form submissions
and displaying filtered dashboard data.

## Technology Stack

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- PyMySQL
- Uvicorn

## Main Feature

Dashboard Filters & Date Range API.

## Dashboard API

GET /dashboard/filters

## Supported Filters

- form_id
- status
- from_date
- to_date
- page
- page_size

## Example

GET /dashboard/filters?form_id=1

## Status Filter

GET /dashboard/filters?status=approved

## Date Range

GET /dashboard/filters?from_date=2026-09-01T00:00:00&to_date=2026-09-03T23:59:59

## Combined Filter

GET /dashboard/filters?form_id=1&status=approved&from_date=2026-09-01T00:00:00&to_date=2026-09-03T23:59:59&page=1&page_size=10

## Run Project

uvicorn app.main:app --reload

## Swagger

http://127.0.0.1:8000/docs