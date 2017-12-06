# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
# from nose_parameterized import parameterized  # 已被重命名
import nose


class TestAdd(unittest.TestCase):

    @parameterized.expand([
        ("01",1, 1, 2),
        ("02",2, 2, 5),
        ("03",3, 3, 6),
    ])
    def test_add(self, name, a, b, c):
        self.assertEqual(a + b, c)


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    # nose.main(defaultTest=__name__)
    nose.run(argv=[__file__, '--with-doctest', '-vv'])  # todo: 这样不行。
    # nose.run(defaultTest=__name__)
