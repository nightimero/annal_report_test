# -*- coding:utf-8 -*-
class AB(object):
    def print_class(self):
        print self.__class__

    # 脱了裤子放屁。
    def print_class2(self):
        print globals()[self.__class__.__name__]

ab = AB()
ab.print_class()
ab.print_class2()

