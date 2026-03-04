from __future__ import annotations

from collections import OrderedDict
from typing import Dict


class LRUCache:
    """
    Simple LRU cache with O(1) operations.

    Backed by OrderedDict: most recently used entries are kept at the end,
    least recently used entry is at the beginning.
    """

    def __init__(self, capacity: int = 10) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._capacity: int = capacity
        self._data: "OrderedDict[str, str]" = OrderedDict()

    def get(self, key: str) -> str:
        """
        Return value by key and mark it as recently used.
        If key is missing, return an empty string.
        """
        if key not in self._data:
            return ""

        value = self._data.pop(key)
        self._data[key] = value
        return value

    def set(self, key: str, value: str) -> None:
        """
        Set value for a key and mark it as recently used.
        When capacity is exceeded, evict the least recently used entry.
        """
        if key in self._data:
            # Refresh existing key and move it to the end
            self._data.pop(key)
        self._data[key] = value

        if len(self._data) > self._capacity:
            # popitem(last=False) -> least recently used entry
            self._data.popitem(last=False)

    def rem(self, key: str) -> None:
        """
        Remove key from the cache if present. No-op otherwise.
        """
        self._data.pop(key, None)


def main() -> None:
    cache = LRUCache(100)
    cache.set("Jesse", "Pinkman")
    cache.set("Walter", "White")
    cache.set("Jesse", "James")

    assert cache.get("Jesse") == "James"
    cache.rem("Walter")
    assert cache.get("Walter") == ""


if __name__ == "__main__":
    main()

