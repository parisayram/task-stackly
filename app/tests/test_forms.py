def test_create_and_get_form(client):
    resp = client.post("/forms", json={"title": "Feedback Form", "description": "test"})
    assert resp.status_code == 201
    form_id = resp.json()["id"]

    resp = client.get(f"/forms/{form_id}")
    assert resp.status_code == 200
    assert resp.json()["title"] == "Feedback Form"


def test_get_missing_form_404(client):
    resp = client.get("/forms/9999")
    assert resp.status_code == 404


def test_add_field_and_validate(client):
    form = client.post("/forms", json={"title": "Signup"}).json()
    field = client.post(
        f"/forms/{form['id']}/fields",
        json={"label": "Age", "field_type": "number", "is_required": True, "validation_rules": {"min": 18}},
    ).json()

    # missing required field
    resp = client.post(f"/forms/{form['id']}/validate", json={})
    assert resp.json()["valid"] is False

    # below min
    resp = client.post(f"/forms/{form['id']}/validate", json={str(field["id"]): 10})
    assert resp.json()["valid"] is False

    # valid
    resp = client.post(f"/forms/{form['id']}/validate", json={str(field["id"]): 21})
    assert resp.json()["valid"] is True


def test_search_forms(client):
    client.post("/forms", json={"title": "Alpha Form"})
    client.post("/forms", json={"title": "Beta Form"})

    resp = client.get("/forms/search", params={"q": "Alpha"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["total"] == 1
    assert body["items"][0]["title"] == "Alpha Form"
