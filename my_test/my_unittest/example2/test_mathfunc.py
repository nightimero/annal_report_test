# -*- coding: utf-8 -*-

import unittest
from mathfunc import *


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    @classmethod
    def setUpClass(cls):
        print 'before testcase exclude'

    @classmethod
    def tearDownClass(cls):
        print 'after testcase finish'

    def setUp(self):
        print 'befor every func'

    def tearDown(self):
        print 'after every func'

    # 可以看到总的test数量还是4个，但divide()
    # 方法被skip了。
    #
    # skip装饰器一共有三个
    # unittest.skip(reason)、unittest.skipIf(condition, reason)、unittest.skipUnless(condition,reason)，
    # skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过。
    @unittest.skip("we just don't want to test add func")
    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.skipTest('jump out the test')  # 虽然跳过了测试方法。但是同样的执行了setup和teardown
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))


def math_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMathFunc('test_multi'))
    suite.addTest(TestMathFunc('test_divide'))
    return suite


if __name__ == '__main__':
    unittest.main()
