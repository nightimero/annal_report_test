# -*- coding: utf-8 -*-
from multiprocessing import Pool
import Queue
import time


def get_number(p):
    time.sleep(0.001)
    if p == 100:
        return True
    else:
        return False
if __name__ == "__main__":
    pool = Pool(processes=10)
    q = Queue.Queue()
    s = time.time()
    for i in xrange(50000):   # 将子进程对象存入队列中。
        q.put(pool.apply_async(get_number, args=(i,)))  # 维持执行的进程总数为10，当一个进程执行完后添加新进程.
    """
    因为这里使用的为pool.apply_async异步方法，因此子进程执行的过程中，父进程会执行while，获取返回值并校验。
    """
    while 1:
        if q.get().get():
            pool.terminate()  # 结束进程池中的所有子进程。
            break
    pool.join()
    e = time.time()
    print u'花费时间：%0.2f' % (e - s)
