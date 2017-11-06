# -*- coding:utf-8 -*-
import time


class PrintTotalTime(object):
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print u'执行测试用例总共耗时{}秒'.format(self.end_time - self.start_time)


with PrintTotalTime() as p:
    time.sleep(3.5)
