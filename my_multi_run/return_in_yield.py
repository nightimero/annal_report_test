# -*- coding:utf-8 -*-
# 因为在生成器中每次迭代都会返回一个值，所以不能显式的在生成器函数中return一个值。
# 设置None也不行。否则会抛出 SyntaxError的异常。
# 但是可以在函数中出现单独的return。那么抛出StopIteration标识终止迭代。
# 例子：
SIZE = 1024
def read_file(path):
    size = 1024
    with open(path,'r') as f:
        while True:
            block = f.read(SIZE)
            if block:
                yield block
            else:
                return
# # 错误
# def test_return():
#     yield 4
#     return 0
#
#   File "<stdin>", line 3
# SyntaxError: 'return' with argument inside generator