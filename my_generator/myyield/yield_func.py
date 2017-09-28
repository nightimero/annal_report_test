# -*- coding:utf-8 -*-
import time


def onerror_retry(exception, callback, timeout=2, timedelta=0.1):
    end_time = time.time() + timeout
    while True:
        try:
            yield callback
            break
        except exception:
            if time.time() > end_time:
                raise
            elif timedelta > 0:
                time.sleep(timedelta)
                print u'重试'


def aa(a):
    print 'in func aa'
    return a + 2


# for retry in onerror_retry(SomeSpecificException, do_stuff):
#	retry()
# 这样没有用啊。获取函数有毛的意思啊。
# https://ask.helplib.com/578565 最后一段
# for retry in onerror_retry(Exception, aa):
#     print 'in for '
#     print retry(3)
# 结果：
# in for
# in func aa
# 5

# 这样才有效果嘛。
for retry in onerror_retry(Exception, aa("3")):
    print retry
# 为什么这里抓不到异常。
# todo： 函数中抛出异常，上级函数抓到异常。