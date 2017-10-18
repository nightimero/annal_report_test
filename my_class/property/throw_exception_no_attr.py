# -*- coding:utf-8 -*-
# 3.同时覆盖掉getattribute和getattr的时候，在getattribute中需要模仿原本的行为抛出AttributeError或者手动调用getattr


class AboutAttr(object):
    def __init__(self, name):
        self.name = name

    # 这个函数没有用。始终不会用到，被__getattribute__中AttributeError拦截了
    def __getattr__(self, item):
        print 'in getattr'
        return 'default'

    def __getattribute__(self, item):
        try:
            return super(AboutAttr, self).__getattribute__(item)
        except KeyError:
            return 'default'
        except AttributeError as ex:
            print ex

at = AboutAttr('test')
print at.name
print at.not_exised


class AboutAttr2(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        try:
            return super(AboutAttr2, self).__getattribute__(item)
        except KeyError:
            return 'default'

    def __getattr__(self, item):
        return 'default get'

at2 = AboutAttr2('test')
print at2.name
print at2.not_exised
