# -*- coding:utf-8 -*-
from . import deractor


@deractor
class A(object):
    def print_h(self):
        print 'hello A'


class C(object):
    def print_h(self):
        print 'hello C'
