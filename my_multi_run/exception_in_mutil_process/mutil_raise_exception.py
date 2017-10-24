# -*- coding:utf-8 -*-
import traceback
from multiprocessing.pool import Pool

# todo: 加上这两行在windows依然不能运行。不加在linux可以运行。
from multiprocessing import freeze_support
freeze_support()

import multiprocessing


# Shortcut to multiprocessing's logger


def error(msg, *args):
    return multiprocessing.get_logger().error(msg, *args)


class LogExceptions(object):
    def __init__(self, callable):
        self.__callable = callable

    def __call__(self, *args, **kwargs):
        try:
            result = self.__callable(*args, **kwargs)

        except Exception as e:
            # Here we add some debugging help. If multiprocessing's
            # debugging is on, it will arrange to log the traceback
            error(traceback.format_exc())
            # Re-raise the original exception so the Pool worker can
            # clean up
            raise

        # It was fine, give a normal answer
        return result


class LoggingPool(Pool):
    def apply_async(self, func, args=(), kwds={}, callback=None):
        return Pool.apply_async(self, LogExceptions(func), args, kwds, callback)


def go():
    print(1)
    raise Exception()
    print(2)

multiprocessing.log_to_stderr()
p = LoggingPool(processes=1)

p.apply_async(go)
p.close()
p.join()
