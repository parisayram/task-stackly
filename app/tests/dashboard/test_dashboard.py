from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_dashboard_summary():
    response = client.get("/dashboard/summary")

    assert response.status_code == 200

    data = response.json()

    assert "total_employees" in data
    assert "active_employees" in data
    assert "total_forms" in data
    assert "total_submissions" in data

    assert data["total_employees"] == 4
    assert data["active_employees"] == 3
    assert data["total_forms"] == 0
    assert data["total_submissions"] == 0