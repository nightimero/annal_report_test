# -*- coding: utf-8 -*-
import unittest
from test_mathfunc import TestMathFunc, math_suite
from test_mycit import dict_suite
from nose import suite
from HtmlTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # a.直接添加
    # suite = unittest.TestSuite((math_suite(), dict_suite()))

    # 一、直接addtest
    # tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    # suite.addTests(tests)

    # 二、使用TestLoader().loadTestsFromName or TestLoader().loadTestsFromNames
    # suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
    # suite.addTests(
    #     unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # loadTestsFromNames()，类似，传入列表

    # 三、使用TestLoader().loadTestFromTestCase
    # loadTestsFromTestCase()，传入TestCase
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    # b.在新建一个suite后，通过addTest的方法
    # suite = unittest.TestSuite()
    # suite.addTest(math_suite())
    # suite.addTest(dict_suite())
    # suite.addTests((math_suite(), dict_suite()))
    my_suite = suite.ContextSuite((math_suite(), dict_suite()))
    runner = unittest.TextTestRunner(verbosity=2)
    # runner = HTMLTestRunner(output='example_suite3')
    runner.run(my_suite)
