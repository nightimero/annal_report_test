# -*- coding:utf-8 -*-
import time
import threading

# 新线程执行的代码:


def loop():
    # current_thread()函数，它永远返回当前线程的实例
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

# 主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
print 'thread %s is running...' % threading.current_thread().name
# 如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
