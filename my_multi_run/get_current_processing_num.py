# -*- coding:utf-8 -*-
import time
from multiprocessing import Pool, freeze_support


def my_sleep(sleep_time):
    time.sleep(sleep_time)
    return 0


if __name__ == '__main__':
    freeze_support()
    pool = Pool(processes=3)
    pool.apply_async(my_sleep, (3,))
    pool.apply_async(my_sleep, (1,))
    pool.apply_async(my_sleep, (5,))

    while True:
        time.sleep(1)
        process_count = len(pool._cache)
        if process_count != 0:
            print "%s processes running" % len(pool._cache)
        else:
            print "all processes are finished"
            break

    pool.close()
    pool.join()
