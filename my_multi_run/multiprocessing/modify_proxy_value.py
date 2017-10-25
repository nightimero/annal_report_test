# -*- coding:utf-8 -*-
# 有趣 。https://linpingta.github.io/blog/2015/03/21/python-manager-dict/
from multiprocessing import Manager, Process
# 还是那句话 最好不要共享数据。


def f1(d):
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
    p = Process(target=f1, args=(d,))
    p.start()
    p.join()
    print d  # {1: 1, 2: {}}

    e = Manager().dict()
    q = Process(target=f2, args=(e,))
    q.start()
    q.join()
    print e  # {1: 1, 2: {2: 3}}
