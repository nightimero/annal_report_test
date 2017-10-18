# -*- coding:utf-8 -*-
import re
# help(iter)
# iter(...)
#     iter(collection) -> iterator
#     iter(callable, sentinel) -> iterator
#
#     Get an iterator from an object.  In the first form, the argument must
#     supply its own iterator, or be a sequence.
#     In the second form, the callable is called until it returns the sentinel.


re.finditer("\d+", "1 ha 2 bah").__class__
# <type 'callable-iterator'>
iter([1, 2]).__class__
# <type 'listiterator'>
iter("hurm").__class__
# <type 'iterator'>
# Two questions:
#
# Is there any meaningful distinction between them?
# Why is the first one called a callable-iterator? You definitely cannot call it.


def globals_are_bad_mmkay():
    global foo
    foo += 2
    return foo

foo = 0
it = iter(globals_are_bad_mmkay, 10)
print list(it)
