# -*- coding:utf-8 -*-
from gevent import monkey
monkey.patch_socket()
import gevent


def f(n):
    for i in range(n):
        print gevent.getcurrent(), i

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g1.start()
g1.join()
g2.start()
g2.join()
