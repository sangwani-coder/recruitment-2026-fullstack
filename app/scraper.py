import requests
from bs4 import BeautifulSoup

URL = "https://www.parliament.gov.zm/members/constituencies"


def scrape_zambia_constituencies() -> dict:
    """
    Scrape provinces and constituencies from the National Assembly of Zambia website.

    Returns:
        dict[str, list[str]]
    """
    response = requests.get(URL, timeout=30, verify=False)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    data = {}

    for province_heading in soup.select("div.view-content > h3"):
        province = province_heading.get_text(strip=True)
        table = province_heading.find_next_sibling("table")

        if not table:
            continue

        constituencies = [
            a.get_text(strip=True)
            for a in table.select("a")
            if a.get_text(strip=True)
        ]

        data[province] = constituencies

    return data
