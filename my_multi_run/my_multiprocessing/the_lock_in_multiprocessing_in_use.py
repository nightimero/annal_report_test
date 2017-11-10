# -*- coding:utf-8 -*-

from multiprocessing import Process, Manager, Lock
import os


def my_func(_sum, cc, lock):
    with lock:
        _sum.value += cc


if __name__ == '__main__':
    threads = []
    lock = Lock()
    manager = Manager()
    _sum = manager.Value('tmp', 0)
    for i in range(100):
        t = Process(target=my_func, args=(_sum, 1, lock))
        t.daemon = True
        threads.append(t)

    for i in range(len(threads)):
        threads[i].start()

    for j in range(len(threads)):
        threads[j].join()

    print "------------------------"
    print 'process id:', os.getpid()
    print _sum.value