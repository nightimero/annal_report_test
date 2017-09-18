# -*- coding: utf-8 -*-
#todo：子进程返回值

from multiprocessing import Pool

def func(p):
    return p

if __name__ == '__main__':
    pool = Pool(processes=4)
    result = []
    for i in xrange(50):
        result.append(pool.apply_async(func,args=(i,)))
    pool.join()

    for i in result:
        print i.get()