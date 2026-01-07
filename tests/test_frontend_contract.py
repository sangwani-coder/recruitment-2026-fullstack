def test_frontend_api_contract(client):
    res = client.get("/api/provinces")
    province = res.json()[0]

    res = client.get(f"/api/constituencies/{province}")
    data = res.json()

    assert "province" in data
    assert "constituencies" in data
    assert isinstance(data["constituencies"], list)
