# -*- coding:utf-8 -*-
import traceback


def func_a():
    print 'func_a'
    print 'func_call_name:'
    print u'调用者的名称是：{}'.format(traceback.extract_stack()[-2][2])



def func_b():
    func_a()
    print 'func_b'

func_b()