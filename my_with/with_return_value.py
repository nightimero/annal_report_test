# -*- coding:utf-8 -*-
import time


class CallButNewReturn(object):
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.return_value = 10
        print u'in init'


class PrintTotalTime(object):
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.return_value = 10
        print u'in init'

    # 如果需要在with中return值，在__enter__中return就好了。
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print u'执行测试用例总共耗时{}秒'.format(self.end_time - self.start_time)

    def __call__(self, *args, **kwargs):
        return self.return_value

a = PrintTotalTime()
print 'call:', a()

with PrintTotalTime() as p:
    print p.return_value
    time.sleep(3.5)
