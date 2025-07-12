import app


def test_home():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data


def test_status():
    client = app.app.test_client()
    response = client.get("/status")
    assert b"OK" in response.data


def test_add():
    client = app.app.test_client()
    response = client.get("/add/3/4")
    assert b"7" in response.data


def test_add_negative():
    client = app.app.test_client()
    response = client.get("/add/-1/1")
    assert b"0" in response.data


def test_not_found():
    client = app.app.test_client()
    response = client.get("/missing")
    assert response.status_code == 404
