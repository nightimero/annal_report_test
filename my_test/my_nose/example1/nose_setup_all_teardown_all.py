# -*- coding: utf-8 -*-
from nose import with_setup  # optional
from nose.tools import raises, assert_raises, nottest, istest

from unnecessary_math import multiply


def setup_module(module):
    print ("")  # this is to get a newline after the dots
    print ("setup_module before anything in this file")


def teardown_module(module):
    print ("teardown_module after everything in this file")


def my_setup_function():
    print ("my_setup_function")


def my_teardown_function():
    print ("my_teardown_function")


@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    print 'test_numbers_3_4  <============================ actual test code'
    assert multiply(3, 4) == 12


@with_setup(my_setup_function, my_teardown_function)
def test_strings_a_3():
    print 'test_strings_a_3  <============================ actual test code'
    assert multiply('a', 3) == 'aaa'


@raises(TypeError, ValueError)
def test_raises_type_error():
    raise TypeError("This test passes")


@raises(Exception)
def test_that_fails_by_passing():
    pass

@nottest
def test_divide_by_zero():
    assert divide(2, 0)

@nottest
def test_divide_by_zero_2():
    assert_raises(ZeroDivisionError, divide, 2, 0)

@istest
def haha():
    assert 4 == 5


class TestUM:
    def setup(self):
        print ("TestUM:setup() before each test method")

    def teardown(self):
        print ("TestUM:teardown() after each test method")

    @classmethod
    def setup_class(cls):
        print ("setup_class() before any methods in this class")

    @classmethod
    def teardown_class(cls):
        print ("teardown_class() after any methods in this class")

    def test_02_numbers_5_6(self):
        print 'test_numbers_5_6()  <============================ actual test code'
        assert multiply(5, 6) == 30

    def test_01_strings_b_2(self):
        print 'test_strings_b_2()  <============================ actual test code'
        assert multiply('b', 2) == 'bb'


        # Alternative names
        #
        # Nose is pretty forgiving about naming conventions for fixtures.
        # I’ll list the alternative names for the different fixtures.
        # However, I strongly encourage you to use the names listed above.
        # The names listed above are, my opinion, easiest to read.
        # The exception to this is setup_function/teardown_function, since those are possibly custom for every test function, use whatever you like.
        #
        # setup_package
        # setup, setUp, or setUpPackage
        # teardown_package
        # teardown, tearDown, or tearDownPackage
        # setup_module
        # setup, setUp, or setUpModule
        # teardown_module
        # teardown, tearDown, or tearDownModule
        # setup_class
        # setupClass, setUpClass, setupAll, or setUpAll
        # teardown_class
        # teardownClass, tearDownClass, teardownAll, or tearDownAll.
        # setup (class method fixtures)
        # setUp
        # teardown (class method fixtures)
        # tearDown
        # setup_function / teardown_function
        # can be named anything, since it’s attached to a function with ‘@with_setup’


 # nosetests -v --with-coverage nose_setup_all_teardown_all.py
 # pip install coverage
 # nosetests -v --with-coverage --with-html-output --html-out-file=./ result1.html nose_setup_all_teardown_al l.py