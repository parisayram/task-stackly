
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


# Helper function: Login and get JWT token
def get_auth_token():
    login_data = {
        "username": "kamesh",
        "password": "kamesh123"
    }

    response = client.post(
        "/auth/login",
        json=login_data
    )

    assert response.status_code == 200

    response_data = response.json()

    assert "access_token" in response_data

    return response_data["access_token"]


# Test 1: Search forms by title
def test_search_forms():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        params={
            "search": "Student"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "page" in data
    assert "size" in data
    assert "total" in data
    assert "pages" in data
    assert "data" in data

    for form in data["data"]:
        assert "student" in form["title"].lower()


# Test 2: Filter active forms
def test_filter_active_forms():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        params={
            "is_active": True
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "data" in data

    for form in data["data"]:
        assert form["is_active"] is True


# Test 3: Filter inactive forms
def test_filter_inactive_forms():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        params={
            "is_active": False
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "data" in data

    for form in data["data"]:
        assert form["is_active"] is False


# Test 4: Pagination
def test_form_pagination():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        params={
            "page": 1,
            "size": 2
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["page"] == 1
    assert data["size"] == 2

    # Page should contain maximum 2 records
    assert len(data["data"]) <= 2



# Test 5: Second page
def test_second_page():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        params={
            "page": 2,
            "size": 2
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["page"] == 2
    assert data["size"] == 2

    assert len(data["data"]) <= 2


# Test 6: Search + filter
def test_search_and_filter():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        params={
            "search": "Registration",
            "is_active": True
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "data" in data

    for form in data["data"]:
        assert "registration" in form["title"].lower()
        assert form["is_active"] is True


# Test 7: Search + filter + pagination
def test_search_filter_pagination():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        params={
            "search": "Registration",
            "is_active": True,
            "page": 1,
            "size": 2
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["page"] == 1
    assert data["size"] == 2

    assert "total" in data
    assert "pages" in data
    assert "data" in data

    assert len(data["data"]) <= 2

    for form in data["data"]:
        assert "registration" in form["title"].lower()
        assert form["is_active"] is True


# Test 8: Search with no matching result
def test_search_no_result():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        params={
            "search": "XYZ_FORM_DOES_NOT_EXIST"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total"] == 0
    assert data["pages"] == 0
    assert data["data"] == []


# Test 9: Default pagination
def test_default_pagination():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["page"] == 1
    assert data["size"] == 10

    assert "total" in data
    assert "pages" in data
    assert "data" in data


# Test 10: Page less than 1
def test_invalid_page():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        params={
            "page": 0,
            "size": 2
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    # Your service changes page < 1 to page 1
    assert data["page"] == 1


# Test 11: Size less than 1
def test_invalid_size():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        params={
            "page": 1,
            "size": 0
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    # Your service changes size < 1 to size 10
    assert data["size"] == 10



# Test 12: Size greater than 100
def test_maximum_size():
    token = get_auth_token()

    response = client.get(
        "/forms/search",
        params={
            "page": 1,
            "size": 200
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    # Your service limits size to 100
    assert data["size"] == 100
