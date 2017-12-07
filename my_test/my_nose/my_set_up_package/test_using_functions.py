# -*- coding: utf-8 -*-
from __future__ import print_function
from nose.tools import with_setup


def setup_module():
    print(__name__, ': setup_module() ~~~~~~~~~~~~~~~~~~~~~~')


def teardown_module():
    print(__name__, ': teardown_module() ~~~~~~~~~~~~~~~~~~~')


def setup_function():
    "attached with 'with_setup'decorator"
    print(__name__, ': setup_function() - - - - - - - - -')


def teardown_function():
    "attached with 'with_setup'decorator"
    print(__name__, ': teardown_function()  - - - - - - -')


def test_func_1():
    print(__name__, ': test_func_1()')


def test_func_2():
    print(__name__, ': test_func_2()')


@with_setup(setup_function, teardown_function)
def test_func_3():
    print(__name__, ': test_func_3()')
