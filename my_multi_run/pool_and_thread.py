# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'shawn'
__mtime__ = '2017/11/10'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from multiprocessing import Pool
import Queue
import threading
import time


def test(p):
    time.sleep(0.001)
    if p == 100:
        return True
    else:
        return False
if __name__ == "__main__":
    result = Queue.Queue()  # 队列
    pool = Pool(processes=10)
    s = time.time()

    def pool_th():
        for i in xrange(50000):  #这里需要创建执行的子进程非常多
            try:
                result.put(pool.apply_async(test, args=(i,)))
            except:
                break

    def result_th():
        while 1:
            a=result.get().get()  # 获取子进程返回值
            if a:
                pool.terminate()  # 结束所有子进程
                break
    '''
    利用多线程，同时运行Pool函数创建执行子进程，以及运行获取子进程返回值函数。
    '''
    t1 = threading.Thread(target=pool_th)
    t2 = threading.Thread(target=result_th)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    pool.join()
    e = time.time()
    print u'花费时间：%0.2f' % (e - s)
