# -*- coding: utf-8 -*-
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from test_mathfunc import TestMathFunc

example_tests = TestLoader().loadTestsFromTestCase(TestMathFunc)

suite = TestSuite([example_tests,])

runner = HTMLTestRunner(output='example_suite')

runner.run(suite)

