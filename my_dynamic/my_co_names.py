# tuple of names of local variables
# However in practice it appears that co_names is a tuple of global variable names
# while co_varnames is a tuple of local variable names (and argument names). For example:

import sys
a = 1

def f(b):
    d = 2
    c = a + b + d
    return c

print(f.__code__.co_varnames)  # prints ('b', 'c')
print(f.__code__.co_names)     # prints ('a',)

def g(b):
    d = 2
    c = a + b + d
    print sys._getframe().f_code.co_name
    print sys._getframe().f_code.co_names
    print sys._getframe().f_code.co_varnames
    return c

g(3)