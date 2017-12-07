# -*- coding: utf-8 -*-
from nose.tools import with_setup


def setup():
    pass


def teardown():
    pass


@with_setup(setup, teardown)
def test_something():
    " ... "
    pass

# Note that with_setup is useful only for test functions, not for test methods or inside of TestCase subclasses.
