import os
import multiprocessing


def double_x(x):
    print 'in func double_x'
    print x*2
    return x*2


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    value = []
    for i in range(4):
        value.append(pool.apply_async(double_x,args=(i,)))
        print value
    pool.close()
    pool.join()
