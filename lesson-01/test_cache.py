import pathlib
import sys
import unittest

THIS_DIR = pathlib.Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from cache import LRUCache


class LRUCacheTests(unittest.TestCase):
    def test_get_from_empty_returns_empty_string(self) -> None:
        cache = LRUCache()
        self.assertEqual(cache.get("missing"), "")

    def test_basic_set_get_and_rem(self) -> None:
        cache = LRUCache(2)
        cache.set("Jesse", "Pinkman")
        cache.set("Walter", "White")

        self.assertEqual(cache.get("Jesse"), "Pinkman")
        self.assertEqual(cache.get("Walter"), "White")

        cache.rem("Walter")
        self.assertEqual(cache.get("Walter"), "")

    def test_updates_value_and_refreshes_usage(self) -> None:
        cache = LRUCache(2)
        cache.set("A", "1")
        cache.set("B", "2")

        # Access A so it becomes most recently used
        self.assertEqual(cache.get("A"), "1")

        # Inserting C should evict B (least recently used)
        cache.set("C", "3")
        self.assertEqual(cache.get("B"), "")
        self.assertEqual(cache.get("A"), "1")
        self.assertEqual(cache.get("C"), "3")

        # Update A and ensure value is updated
        cache.set("A", "10")
        self.assertEqual(cache.get("A"), "10")

    def test_respects_capacity_and_eviction_order(self) -> None:
        cache = LRUCache(3)
        cache.set("one", "1")
        cache.set("two", "2")
        cache.set("three", "3")

        # Touch "one" and "two" so "three" becomes LRU
        self.assertEqual(cache.get("one"), "1")
        self.assertEqual(cache.get("two"), "2")

        cache.set("four", "4")

        # "three" should be evicted
        self.assertEqual(cache.get("three"), "")
        self.assertEqual(cache.get("one"), "1")
        self.assertEqual(cache.get("two"), "2")
        self.assertEqual(cache.get("four"), "4")

    def test_capacity_must_be_positive(self) -> None:
        with self.assertRaises(ValueError):
            LRUCache(0)


if __name__ == "__main__":
    unittest.main()

