def find_province_by_constituency(
    data: dict[str, list[str]],
    constituency_name: str
) -> str | None:
    """
    Given scraped data and a constituency name,
    return the province it belongs to.

    Case-insensitive.

    Returns:
        province name if found, otherwise None
    """
    raise NotImplementedError
