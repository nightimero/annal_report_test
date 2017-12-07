# -*- coding: utf-8 -*-
# Tools for testing
from nose.tools import *

nose.tools provides a few convenience functions to make writing tests easier. You don’t have to use them; nothing in the rest of nose depends on any of these methods.

nose.tools.ok_(expr, msg=None)
Shorthand for assert. Saves 3 whole characters!

nose.tools.eq_(a, b, msg=None)
Shorthand for ‘assert a == b, “%r != %r” % (a, b)

nose.tools.make_decorator(func)
Wraps a test decorator so as to properly replicate metadata of the decorated function, including nose’s additional stuff (namely, setup and teardown).

nose.tools.raises(*exceptions)
Test must raise one of expected exceptions to pass.

Example use:

@raises(TypeError, ValueError)
def test_raises_type_error():
    raise TypeError("This test passes")

@raises(Exception)
def test_that_fails_by_passing():
    pass
If you want to test many assertions about exceptions in a single test, you may want to use assert_raises instead.

nose.tools.set_trace()
Call pdb.set_trace in the calling frame, first restoring sys.stdout to the real output stream. Note that sys.stdout is NOT reset to whatever it was before the call once pdb is done!

nose.tools.timed(limit)
Test must finish within specified time limit to pass.

Example use:

@timed(.1)
def test_that_fails():
    time.sleep(.2)
nose.tools.with_setup(setup=None, teardown=None)
Decorator to add setup and/or teardown methods to a test function:

@with_setup(setup, teardown)
def test_something():
    " ... "
Note that with_setup is useful only for test functions, not for test methods or inside of TestCase subclasses.

nose.tools.istest(func)
Decorator to mark a function or method as a test

nose.tools.nottest(func)
Decorator to mark a function or method as not a test
