# -*- coding: utf-8 -*-
import unittest
from tkinter import Widget


class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("The widget")


class DefaultWidgetSizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        assert self.widget.size() == (50, 50), 'incorrect default size'


class WidgetResizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.widget.resize(100, 150)
        assert self.widget.size() == (100, 150), \
            'wrong size after resize'


# 测试异常
#
# 测试经常希望检查在某个环境中是否出现异常。如果期待的异常没有抛出，测试将失败。这很容易做到：

def runTest(self):
    try:
        self.widget.resize(-1, -1)
    except ValueError:
        pass
    else:
        fail("expected a ValueError")


# 通常，预期异常源（译者注：将抛出异常的代码）是一个可调用对象；为此，TestCase有一个assertRaises方法。
# 此方法的前两个参数是应该出现在“except”语句中的异常和可调用对象。剩余的参数是应该传递给可调用对象的参数。

def runTest(self):
    self.assertRaises(ValueError, self.widget.resize, -1, -1)
