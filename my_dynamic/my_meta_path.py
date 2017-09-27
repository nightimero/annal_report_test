# -*- coding:utf-8 -*-
# todo: https://mozillazg.github.io/2016/04/apm-python-agent-principle.html
# import sys
#
#
# class MetaPathFinder:
#
#     def find_module(self, fullname, path=None):
#         print('find_module {}'.format(fullname))
#         return MetaPathLoader()
#
#
# class MetaPathLoader:
#
#     def load_module(self, fullname):
#         print('load_module {}'.format(fullname))
#         sys.modules[fullname] = sys
#         return sys
#
# sys.meta_path.insert(0, MetaPathFinder())
#
# if __name__ == '__main__':
#     import http
#     print(http)
#     print(http.version_info)


# =======================================================================

import functools
import time


def func_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('start func')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('spent {}s'.format(end - start))
        return result
    return wrapper


def sleep(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    func = func_wrapper(sleep)
    print(func(3))