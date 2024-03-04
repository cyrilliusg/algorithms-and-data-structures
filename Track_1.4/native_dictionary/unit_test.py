import unittest
from native_dictionary import NativeDictionary


class TestNativeDictionary(unittest.TestCase):
    def setUp(self):
        self.nd = NativeDictionary(10)

    def test_put_new_key(self):
        self.nd.put("key1", "value1")
        self.assertEqual(self.nd.get("key1"), "value1")

    def test_put_existing_key(self):
        self.nd.put("key1", "value1")
        self.nd.put("key1", "value2")
        self.assertEqual(self.nd.get("key1"), "value2")

    def test_is_key_present(self):
        self.nd.put("key1", "value1")
        self.assertTrue(self.nd.is_key("key1"))

    def test_is_key_absent(self):
        self.assertFalse(self.nd.is_key("key2"))

    def test_get_existing_key(self):
        self.nd.put("key1", "value1")
        self.assertEqual(self.nd.get("key1"), "value1")

    def test_get_absent_key(self):
        self.assertIsNone(self.nd.get("key2"))


if __name__ == '__main__':
    unittest.main()
