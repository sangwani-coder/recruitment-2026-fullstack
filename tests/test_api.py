def test_get_provinces(client):
    res = client.get("/api/provinces")
    assert res.status_code == 200
    assert isinstance(res.json(), list)


def test_invalid_province(client):
    res = client.get("/api/constituencies/InvalidProvince")
    assert res.status_code == 404
