# -*- coding:utf-8 -*-

# todo: http://www.jb51.net/article/61454.htm 2017-10-9
# todo: http://www.cnblogs.com/cicaday/p/python-decorator.html 2017-10-9
# todo: http://blog.csdn.net/u013679490/article/details/54772863 2017-10-9
# todo: http://www.cnblogs.com/lovesqcc/p/4060277.html 2017-10-9
# todo: http://blog.csdn.net/hello_katty/article/details/46591463 2017-10-9

# todo: http://blog.csdn.net/orangleliu/article/details/43308397 2017-10-9 try it


# 用两个装饰器inspect参数，叠加使用错误。可以改正吗？获取到函数参数。
import time
from config.global_config import *
import random
import logging
import inspect
from functools import wraps

logging.basicConfig(level=logging.WARNING,
                format='%(message)s',
                filename='myapp.log',
                filemode='w')

#todo: assert 后继续运行
#todo：添加到jenkins上自动执行，返回结果打印到jenkins上
#todo：打开聊天首页，图片无法加载，导致浏览器一直在加载。导致无法运行后续测试代码。


def log_send_msg(log_level=False):
    def deractor(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            funcargs = inspect.getcallargs(func, *args, **kwargs)
            print u'log_msg', funcargs
            sendmsg = funcargs.get('sendmsg')
            result = func(*args, **kwargs)
            if log_level and result:
                logging.warning(sendmsg)
        return wrap
    return deractor

def assert_send_msg(assert_level=False):
    def deractor(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            funcargs = inspect.getcallargs(func, *args, **kwargs)
            print u'assert_msg', funcargs
            sendmsg = funcargs.get('sendmsg')
            result = func(*args, **kwargs)
            if assert_level and result:
                print '*****************+++++++++++++++++++'
                raise Exception(u'发送消息错误', u'发送的消息：%s' % sendmsg)
        return wrap
    return deractor