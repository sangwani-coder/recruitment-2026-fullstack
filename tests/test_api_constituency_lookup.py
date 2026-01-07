def test_lookup_constituency_success(client):
    provinces = client.get("/api/provinces").json()
    province = provinces[0]

    res = client.get(f"/api/constituencies/{province}")
    constituency = res.json()["constituencies"][0]

    lookup = client.get(f"/api/constituency/{constituency}")
    assert lookup.status_code == 200

    data = lookup.json()
    assert data["province"] == province
    assert data["constituency"] == constituency


def test_lookup_constituency_not_found(client):
    res = client.get("/api/constituency/DoesNotExist")
    assert res.status_code == 404
