# -*- coding: utf-8 -*-
"""
Module showing how doctests can be included with source code
Each '>>>' line is run as if in a python shell, and counts as a test.
The next line, if not '>>>' is the expected output of the previous line.
"""


def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b


def divide(a, b):
    print 'divide'
    return a / b


def haha():
    print 'haha'

#
# Trying:
#     multiply(4, 3)
# Expecting:
#     12
# ok
# Trying:
#     multiply('a', 3)
# Expecting:
#     'aaa'
# ok
# 1 items had no tests:
#     unnecessary_math
# 1 items passed all tests:
#    2 tests in unnecessary_math.multiply
# 2 tests in 2 items.
# 2 passed and 0 failed.
# Test passed.
