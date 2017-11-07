# -*- coding:utf-8 -*-
import traceback
import sys


def func_a():
    print 'func_a'
    print 'func_call_name:'
    print u'调用者的名称是：{}'.format(traceback.extract_stack()[-2][2])
    print sys._getframe().f_code.co_name


def func_b():
    func_a()
    print 'func_b'

func_b()