# -*- coding: utf-8 -*-
import unittest


class MyClass(unittest.TestCase):
    def delf(self, a):
        print a

    @classmethod
    def set_resource(self):
        print 'set_resource'

    @classmethod
    def setUpClass(cls):
        print "setUpclass"
        cls.set_resource()

    def setUp(self):
        print "setUp"

        floating_ip = ('setUptoTearDwon',)
        self.addCleanup(self.delf,
                        floating_ip[0])

    def test_1(self):
        '''i dont konw'''
        a = '1111'
        print "test_1"

        floating_ip = ('bbbbb',)
        self.addCleanup(self.delf,
                        floating_ip[0])
        print "2222"
        self.addCleanup(self.delf,
                        a)

    def tearDown(self):
        print 'this is tearDown'

    def test_2(self):
        print "test_2"

    @classmethod
    def tearDownClass(cls):
        print "teardown...."

# 用pytest运行时，结果如下，没有识别到setUpclass

# self.addCleanup()

# def set_resource()


# py.test -k 详解
#
# py.test -k "method_a or method_b"
# 测试类或函数包含 method_a 或 method_b 中的测试将被运行
#
# py.test -k "SomeClass and no method_a"
# 测试类名包含 SomeClass，并且该测试类中包含 method_a 将被跳过
#
# 获取程序输出
#
# py.test -s	# = capature=no，将不捕获输出，直接打印


# python -m nose example4 -v -s