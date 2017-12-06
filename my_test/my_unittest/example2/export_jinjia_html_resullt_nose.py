# -*- coding: utf-8 -*-
# from unittest import TestLoader, TestSuite
from nose import loader, suite
from HtmlTestRunner import HTMLTestRunner
from test_mathfunc import TestMathFunc

# example_tests = TestLoader().loadTestsFromTestCase(TestMathFunc)
example_tests = loader.TestLoader().loadTestsFromTestCase(TestMathFunc)

# suite = TestSuite([example_tests,])
suite = suite.ContextSuite([example_tests, ])

# runner = HTMLTestRunner(output='example_suite2')
# runner.run(suite)
with open('HTMLReport.html', 'w') as f:
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            output='example_suite3'
                            )
    runner.run(suite)



