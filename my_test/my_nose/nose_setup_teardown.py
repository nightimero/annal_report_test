# -*- coding: utf-8 -*-

from nose import with_setup  # optional

def multiply():
    pass


def my_setup_function():
    pass


def my_teardown_function():
    pass


@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    assert multiply(3, 4) == 12




def my_setup_function():
    pass


def my_teardown_function():
    pass


@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    assert multiply(3, 4) == 12


# If you don’t like to use decorators, you can also assign the setup and teardown attributes like this:

test_numbers_3_4.setup = my_setup_function
test_numbers_3_4.teardown = my_teardown_function


class TestUM:
    @classmethod
    def setup_class(cls):
        print ("setup_class() before any methods in this class")

    @classmethod
    def teardown_class(cls):
        print ("teardown_class() after any methods in this class")