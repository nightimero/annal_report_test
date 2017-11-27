# -*- coding:utf-8 -*-
# 演示的好。 https://my.oschina.net/leejun2005/blog/203148
# list.append() 不会有冲突的问题。 sum+= 会有冲突的问题
from multiprocessing import Process, Manager
import os
# todo: 你能信， manager = Manager() 放在这里就会出错。在windows中，必须要放在if __name__ == '__main__':后
# 为什么？
# manager = Manager()
# _sum = manager.Value('tmp', 0)


def my_func(_sum, cc):
    _sum.value += cc

# manager = Manager()
# _sum = manager.Value('tmp', 0)
if __name__ == '__main__':
    threads = []
    manager = Manager()
    _sum = manager.Value('tmp', 0)

    for i in range(100):
        t = Process(target=my_func, args=(_sum, 1,))
        t.daemon = True  # todo:t.daemon 是什么意思？
        threads.append(t)

    for i in range(len(threads)):
        threads[i].start()

    for j in range(len(threads)):
        threads[j].join()

    print "------------------------"
    print 'process id:', os.getpid()
    print _sum.value
# todo：没加锁，在Linux中结果随机了。丢失了一部分加的值。都是赋值导致的。 但是windows中是对的。哈哈哈哈 泪。 错了，windows中也错了。概率低而已。
#     应该是什么问题呢？
# 也许你会问：WTF？其实这个问题在多线程时代就存在了，只是在多进程时代又杯具重演了而已：Lock！