# -*- coding:utf-8 -*-

# todo: http://www.cnblogs.com/codingmylife/p/3630701.html
# todo: contextlib how to use
from decorator import FunctionMaker, decorator
from contextlib import contextmanager


@contextmanager
def rename_scope(obj, new_name):
    """ A rename scope to rename obj's __name__, restore __name__when exit. """
    old_name = obj.__name__
    obj.__name__ = new_name
    yield
    obj.__name__ = old_name


def newcaller(caller, sig_func):
    """ Generate a new caller using sig_func signatures, doc and name, etc. """
    evaldict = sig_func.func_globals.copy()
    evaldict['_call_'] = caller
    return FunctionMaker.create(
        sig_func, "return _call_(%(shortsignature)s)",
        evaldict, signature=sig_func)


def signature(sig_func, copy_name=False):
    """ A decorator to update function signature, doc by sig_func. If copy_name, the return function use sig_func name else function keep its name. """

    def sig_wrapper(caller):
        with rename_scope(sig_func, sig_func.__name__ if copy_name else caller.__name__):
            return newcaller(caller, sig_func)

    return sig_wrapper
