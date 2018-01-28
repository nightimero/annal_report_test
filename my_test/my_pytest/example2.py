# -*- coding: utf-8 -*-
from __future__ import print_function
import allure


def setup_module(module):
    print('\nsetup_module()')


def teardown_module(module):
    print('teardown_module()')


def setup_function(function):
    print('\nsetup_function()')


def teardown_function(function):
    print('\nteardown_function()')


@allure.step('test_step')
def test_1():
    print('-  test_1()')


def test_2():
    print('-  test_2()')

# py.test example2.py::test_1 -s  # -s 打印所有内容到控制台。
