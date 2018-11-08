import requests


def test_heartbeat(endpoint):
    url = endpoint + "__heartbeat__"
    resp = requests.get(url)
    data = resp.json()

    assert resp.status_code == 200
    assert "code" in data
    assert data["database"] == "ok"
    assert data["status"] == "ok"


def test_version(endpoint):
    url = endpoint + "__version__"
    resp = requests.get(url)
    data = resp.json()
    expected_fields = ["commit", "version", "source", "build"]

    assert resp.status_code == 200

    for field in expected_fields:
        assert field in data
