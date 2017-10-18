# -*- coding:utf-8 -*-

# 含有 __iter__() 方法或 __getitem__() 方法的对象称之为可迭代对象。
# 我们可以使用 Python 内置的 hasattr() 函数来判断一个对象是不是可迭代的：
hasattr((), '__iter__')
True
hasattr([], '__iter__')
True
hasattr({}, '__iter__')
True
hasattr(123, '__iter__')
False
hasattr('abc', '__iter__')
False
hasattr('abc', '__getitem__')
True

# 另外，我们也可使用 isinstance() 进行判断：

from collections import Iterable

isinstance((), Iterable)        # 元组
True
isinstance([], Iterable)        # 列表
True
isinstance({}, Iterable)        # 字典
True
isinstance('abc', Iterable)     # 字符串
True
isinstance(100, Iterable)       # 数字
False

# 迭代器协议（iterator protocol）是指要实现对象的 __iter()__ 和 next() 方法
# （注意：Python3 要实现 __next__() 方法），
# 其中，__iter()__ 方法返回迭代器对象本身，
# next() 方法返回容器的下一个元素，在没有后续元素时抛出 StopIteration 异常。


hasattr((1, 2, 3), '__iter__')
True
hasattr((1, 2, 3), 'next')  # 有 __iter__ 方法但是没有 next 方法，不是迭代器
False

hasattr([1, 2, 3], '__iter__')
True
hasattr([1, 2, 3], 'next')
False

hasattr({'a': 1, 'b': 2}, '__iter__')
True
hasattr({'a': 1, 'b': 2}, 'next')
False

# 同样，我们也可以使用 isinstance() 进行判断：

from collections import Iterator

isinstance((), Iterator)
False
isinstance([], Iterator)
False
isinstance({}, Iterator)
False
isinstance('', Iterator)
False
isinstance(123, Iterator)
False


# 可见，虽然元组、列表和字典等对象是可迭代的，但它们却不是迭代器！
# 对于这些可迭代对象，可以使用 Python 内置的 iter() 函数获得它们的迭代器对象，看下面的使用：

from collections import Iterator
isinstance(iter([1, 2, 3]), Iterator)  # 使用 iter() 函数，获得迭代器对象
True
isinstance(iter('abc'), Iterator)
True

my_str = 'abc'
next(my_str)      # my_str 不是迭代器，不能使用 next()，因此出错
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-15-5f369cd8082f> in <module>()
# ----> 1 next(my_str)

# TypeError: str object is not an iterator

my_iter = iter(my_str)   # 获得迭代器对象
isinstance(my_iter, Iterator)
True
next(my_iter)   # 可使用内置的 next() 函数获得下一个元素
'a'

# 事实上，Python 的 for 循环就是先通过内置函数 iter() 获得一个迭代器，然后再不断调用 next() 函数实现的，比如：

for x in [1, 2, 3]:
    print x
# 等价于

# 获得 Iterator 对象
it = iter([1, 2, 3])

# 循环
while True:
    try:
        # 获得下一个值
        x = next(it)
        print x
    except StopIteration:
        # 没有后续元素，退出循环
        break
