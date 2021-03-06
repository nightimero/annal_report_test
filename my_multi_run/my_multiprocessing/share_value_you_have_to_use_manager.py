# -*- coding:utf-8 -*-
from multiprocessing import Process, Manager
import os


def my_func(list_a, cc):
    list_a.append(cc)
    # vip_list[cc] = cc  # windows系统中使用这样的全局会报错。linux不会。
    print 'process id:', os.getpid()

if __name__ == '__main__':
    threads = []

    # freeze_support()  # 加上了还是报错。咋回事呢？  # todo：freeze_support() 在什么时候起作用

    manager = Manager()
    # vip_list = []  # 如果这样写的话，就会错 最后list是空的。
    vip_list = manager.list()
    for i in range(10):
        t = Process(target=my_func, args=(vip_list, i,))
        t.daemon = True
        threads.append(t)

    for i in range(len(threads)):
        threads[i].start()

    for j in range(len(threads)):
        threads[j].join()

    print "------------------------"
    print 'process id:', os.getpid()
    print vip_list
