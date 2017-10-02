# -*- coding:utf-8 -*-

# 参考： https://stackoverflow.com/questions/19287066/difference-between-callable-iterator-and-listiterator-and-iterator
# todo: 为什么会这样 iter(callable,sentinel)
# >>> help(iter)
# iter(...)
#     iter(collection) -> iterator
#     iter(callable, sentinel) -> iterator
#
#     Get an iterator from an object.  In the first form, the argument must
#     supply its own iterator, or be a sequence.
#     In the second form, the callable is called until it returns the sentinel.

def globals_are_bad_mmkay():
    global foo
    foo += 2
    return foo

foo = 0
it = iter(globals_are_bad_mmkay, 10)
print list(it)
