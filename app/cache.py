from typing import Dict

_cache: Dict[str, list] | None = None


def get_cache():
    return _cache


def set_cache(data: Dict[str, list]):
    global _cache
    _cache = data
