from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_permission():
    response = client.post(
        "/forms/1/permissions",
        json={
            "form_id": 1,
            "employee_id": 1,
            "can_view": True,
            "can_submit": True,
            "can_edit": False,
            "can_delete": False
        }
    )

    assert response.status_code == 201


def test_get_permissions():
    response = client.get("/forms/1/permissions")

    assert response.status_code == 200


def test_update_permission():
    response = client.put(
        "/forms/1/permissions/1",
        json={
            "can_view": True,
            "can_submit": True,
            "can_edit": True,
            "can_delete": True
        }
    )

    assert response.status_code == 200


def test_delete_permission():
    response = client.delete("/forms/1/permissions/1")

    assert response.status_code == 200