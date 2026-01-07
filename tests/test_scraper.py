from app.scraper import scrape_zambia_constituencies


def test_scraper_returns_dict():
    data = scrape_zambia_constituencies()
    assert isinstance(data, dict)
    assert len(data) > 0
