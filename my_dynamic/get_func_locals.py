# -*- coding:utf-8 -*-
import sys

def case7():
    """
    姓名 - 多问法进入姓名测试
    """
    who_i_ams = []
    who_i_am_1 = [u'我叫%s' % x for x in (u'什么', u'啥',)]
    who_i_am_2 = [u'我是谁']
    # x,y,z = ((1),(2),(3,4)) x = 1 ,y = 2, z=(3,4) 不符合要求，应该是x,y,z = ((1,),(2,),(3,4))，这样x,y,z都是元组
    who_i_am_3 = [u'我{0}{1}是{2}'.format(x, y, z) for x in (u'的', u'',) for y in (u'名字', u'姓名',) for z in (u'什么', u'啥',)]
    who_i_am_4 = [u'{}我{}{}'.format(x, y, z) for x in (u'请问', u'你知道',) for y in (u'的', u'',) for z in (u'名字', u'姓名',)]
    who_i_am_5 = [u'我{}{}'.format(x, y) for x in (u'的', u'',) for y in (u'名字', u'姓名',)]
    who_i_am_6 = [u'{}呢'.format(x) for x in (u'名字', u'姓名',)]


print case7.__code__.co_name
print case7.__code__.co_varnames
print case7.__code__.co_cellvars
print case7.__code__.co_nlocals
