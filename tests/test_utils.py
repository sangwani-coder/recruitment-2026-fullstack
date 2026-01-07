from app.utils import find_province_by_constituency


def test_find_province_success():
    data = {
        "Lusaka": ["Matero", "Kanyama"],
        "Central": ["Bwacha"]
    }

    province = find_province_by_constituency(data, "Matero")
    assert province == "Lusaka"


def test_find_province_case_insensitive():
    data = {
        "Lusaka": ["Matero", "Kanyama"]
    }

    province = find_province_by_constituency(data, "matero")
    assert province == "Lusaka"


def test_find_province_not_found():
    data = {
        "Lusaka": ["Matero"]
    }

    province = find_province_by_constituency(data, "Unknown")
    assert province is None
