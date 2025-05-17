import unittest
import os
from unittest.mock import patch
from envil import (
    get_int,
    get_float,
    get_bool,
    get_str,
    EnvironmentVariableNotSet,
)


class TestEnvironmentGetters(unittest.TestCase):

    @patch.dict(os.environ, {"TEST_INT": "42"})
    def test_get_int_present(self):
        self.assertEqual(get_int("TEST_INT"), 42)

    def test_get_int_default(self):
        self.assertEqual(get_int("MISSING_INT", default=7), 7)

    def test_get_int_missing_raises(self):
        with self.assertRaises(EnvironmentVariableNotSet):
            get_int("MISSING_INT")

    @patch.dict(os.environ, {"TEST_FLOAT": "3.14"})
    def test_get_float_present(self):
        self.assertAlmostEqual(get_float("TEST_FLOAT"), 3.14)

    def test_get_float_default(self):
        self.assertEqual(get_float("MISSING_FLOAT", default=2.71), 2.71)

    def test_get_float_missing_raises(self):
        with self.assertRaises(EnvironmentVariableNotSet):
            get_float("MISSING_FLOAT")

    @patch.dict(os.environ, {"TEST_BOOL_TRUE": "yes", "TEST_BOOL_FALSE": "no"})
    def test_get_bool_present(self):
        self.assertTrue(get_bool("TEST_BOOL_TRUE"))
        self.assertFalse(get_bool("TEST_BOOL_FALSE"))

    def test_get_bool_default(self):
        self.assertTrue(get_bool("MISSING_BOOL", default=True))
        self.assertFalse(get_bool("MISSING_BOOL", default=False))

    def test_get_bool_custom_falsy(self):
        with patch.dict(os.environ, {"MY_BOOL": "nah"}):
            self.assertFalse(get_bool("MY_BOOL", falsy_strings={"nah"}))

    def test_get_bool_missing_raises(self):
        with self.assertRaises(EnvironmentVariableNotSet):
            get_bool("MISSING_BOOL")

    @patch.dict(os.environ, {"TEST_STR": "hello"})
    def test_get_str_present(self):
        self.assertEqual(get_str("TEST_STR"), "hello")

    def test_get_str_default(self):
        self.assertEqual(get_str("MISSING_STR", default="world"), "world")

    def test_get_str_missing_raises(self):
        with self.assertRaises(EnvironmentVariableNotSet):
            get_str("MISSING_STR")


if __name__ == "__main__":
    unittest.main()
