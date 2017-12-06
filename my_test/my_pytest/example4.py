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
