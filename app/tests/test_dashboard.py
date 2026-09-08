def test_dashboard_summary_empty(client):
    resp = client.get("/dashboard/summary")
    assert resp.status_code == 200
    body = resp.json()
    assert body["total_forms"] == 0
    assert body["total_submissions"] == 0


def test_dashboard_summary_after_form_created(client):
    client.post("/forms", json={"title": "Test Form"})
    resp = client.get("/dashboard/summary")
    assert resp.json()["total_forms"] == 1
    assert resp.json()["active_forms"] == 1


def test_export_csv(client):
    resp = client.get("/dashboard/export", params={"format": "csv"})
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/csv")
