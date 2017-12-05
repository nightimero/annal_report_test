# -*- coding: utf-8 -*-
import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()

    # 一、直接addtest
    # tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    # suite.addTests(tests)

    # 二、使用TestLoader().loadTestsFromName or TestLoader().loadTestsFromNames
    # suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
    # suite.addTests(
    #     unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # loadTestsFromNames()，类似，传入列表

    # 三、使用TestLoader().loadTestFromTestCase
    # loadTestsFromTestCase()，传入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
