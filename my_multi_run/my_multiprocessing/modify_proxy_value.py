# -*- coding:utf-8 -*-
# 有趣 。https://linpingta.github.io/blog/2015/03/21/python-manager-dict/
from multiprocessing import Manager, Process, Pool
import psutil
import os
import time

# 还是那句话 最好不要共享数据。


def f1(d):
    print 'id:', id(d)
    d[1] = 1
    d[2] = {}
    d[2][2] = 3


def f2(e):
    e[1] = 1
    t = {}
    t[2] = 3
    e[2] = t


if __name__ == '__main__':
    d = Manager().dict()  # 进程间共享dict
    for i in range(1000000):
        d[i] = i
    pool = Pool(processes=50)
    pool.apply_async(f1, d)

    # p = Process(target=f1, args=(d,))
    # p2 = Process(target=f1, args=(d,))
    # p3 = Process(target=f1, args=(d,))
    # p.start()
    # p2.start()
    # p3.start()
    # p.join()
    # p2.join()
    # p3.join()
    # # print d  # {1: 1, 2: {}}
    time.sleep(120)
    proc = psutil.Process(os.getpid())
    print 'children:', proc.children()
    for sub_proc in proc.children():
        print 'child memory', sub_proc.memory_info()[0]/(1024*1024)
    print 'memory:', proc.memory_info()[0]/(1024*1024)
    pool.close()
    pool.join()

    # e = Manager().dict()
    # q = Process(target=f2, args=(e,))
    # q.start()
    # q.join()
    # print e  # {1: 1, 2: {2: 3}}
