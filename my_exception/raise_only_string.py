# -*- coding:utf-8 -*-

raise "Exception string"
# 把字符串当成异常抛出看上去是一个非常简洁的办法，但其实是一个非常不好的习惯。

if is_work_done():
    pass
else:
    raise "Work is not done!" # not cool
# 上面的语句如果抛出异常，那么会是这样的：
#
# Traceback (most recent call last):
#   File "/demo/exception_hanlding.py", line 48, in <module>
#     raise "Work is not done!"
# TypeError: exceptions must be old-style classes or derived from BaseException, not str
# 这在 Python2.4 以前是可以接受的做法，但是没有指定异常类型有可能会让下游没办法正确捕获并处理这个异常，
    # 从而导致你的程序难以维护。简单说，这种写法是是封建时代的陋习，应该扔了。