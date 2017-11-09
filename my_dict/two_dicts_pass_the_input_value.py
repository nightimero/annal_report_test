# -*- coding:utf-8 -*-


def print_b(**kwargs1):
    print 'print_b', kwargs1
    print 'print_b,a:', kwargs1['a']


def print_c(**kwargs2):
    print 'print_c', kwargs2
    print 'print_c,d:', kwargs2['d']


def print_a(**kwargs1, **kwargs2):
        # SyntaxError: invalid
        # syntax
        # 不能这样写，第二个字典是无法收集到数据的。
    print kwargs1['a']
    print kwargs1['b']
    print kwargs1['c']
    print_b(**kwargs1)
    print_b(**kwargs2)








dict_a = {'a': 1,
          'b': 2,
          'c': 3,
          }

print_a(**dict_a)

print_a(a=2, b=3, c=4)