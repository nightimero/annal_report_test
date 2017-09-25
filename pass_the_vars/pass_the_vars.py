# -*- coding:utf-8 -*-

def print_everything(*args):
    for count, thing in enumerate(args):
        print( '{0}. {1}'.format(count, thing))

print_everything('apple', 'banana', 'cabbage')
# 0. apple
# 1. banana
# 2. cabbage
# Similarly, **kwargs allows you to handle named arguments that you have not defined in advance:

def table_things(**kwargs):
    for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))

table_things(apple = 'fruit', cabbage = 'vegetable')
# cabbage = vegetable
# apple = fruit
# You can use these along with named arguments too. The explicit arguments get values first and then everything else is passed to *args and **kwargs. The named arguments come first in the list. For example:

# def table_things(titlestring, **kwargs)
# You can also use both in the same function definition but *args must occur before **kwargs.

# You can also use the * and ** syntax when calling a function. For example:

def print_three_things(a, b, c):
    print( 'a = {0}, b = {1}, c = {2}'.format(a,b,c))

mylist = ['aardvark', 'baboon', 'cat']
print_three_things(*mylist)
# a = aardvark, b = baboon, c = cat


class Foo(object):
    def __init__(self, value1, value2):
        # do something with the values
        print value1, value2

class MyFoo(Foo):
    def __init__(self, *args, **kwargs):
        # do something else, don't care about the args
        print 'myfoo'
        super(MyFoo, self).__init__(*args, **kwargs)