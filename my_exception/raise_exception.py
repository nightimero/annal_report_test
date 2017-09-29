# -*- coding:utf-8 -*-
import sys
reload(sys)
print sys.getdefaultencoding()
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

def run_case(run_case_method):
    if run_case_method == 1:
        print run_case_method
    elif run_case_method == 2:
        print run_case_method
    elif run_case_method == 3:
        print run_case_method
    else:
        # 换行无法正确的显示完exception的msg
        # raise Exception(u"错误的跑用例方式，正确的只有1-所有,"
        #                 u"2-根据测试集,3-按照排除的测试集", run_case_method)
        raise Exception(u"错误的跑用例方式，正确的只有1-所有,2-根据测试集,3-按照排除的测试集", run_case_method)

run_case(44)
