# -*- coding: utf-8 -*-
import unittest
from nose_parameterized import parameterized


class TestAdd(unittest.TestCase):

    @parameterized.expand([
        ("01",1, 1, 2),
        ("02",2, 2, 5),
        ("03",3, 3, 6),
    ])
    def test_add(self, name, a, b, c):
        self.assertEqual(a + b, c)


if __name__ == '__main__':
    unittest.main(verbosity=2)
