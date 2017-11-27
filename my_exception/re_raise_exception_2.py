# -*- coding:utf-8 -*-
# 在Python2中，为了保持异常的完整信息，那么你捕获后再次抛出时千万不能在raise后面加上异常对象，
# 否则你的trace信息就会从此处截断。以上是最简单的重新抛出异常的做法，也是推荐的做法。
#
# 还有一些技巧可以考虑，比如抛出异常前你希望对异常的信息进行更新。


def f1():
    print(1/0)


def f2():
    try:
        f1()
    except Exception as e:
        e.args += ('more info',)
        raise

f2()
