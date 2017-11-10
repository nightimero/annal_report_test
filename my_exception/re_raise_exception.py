# -*- coding:utf-8 -*-
# 传递异常 re-raise Exception
# 捕捉到了异常，但是又想重新抛出它（传递异常），使用不带参数的raise语句即可：

def f1():
    print(1/0)

def f2():
    try:
        f1()
    except Exception as e:
        raise  # don't raise e !!!

f2()
