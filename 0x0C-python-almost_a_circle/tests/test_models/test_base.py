#!/usr/bin/python3
"""
My test_base module
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
     my test class for Base class
    """
    def test_0(self):
        """
        test_0
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)


if __name__ == '__main__':
    unittest.main()
