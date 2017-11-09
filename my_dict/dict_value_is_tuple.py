# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

def print_b(**kwargs):
    print 'print_b', kwargs
    print 'print_b,a:', kwargs['a']


def print_a(**kwargs):
    print kwargs['a']
    print kwargs['b']
    print kwargs['c']
    b_kwargs = kwargs
    b_kwargs['a'] = 100
    print_b(**b_kwargs)


dict_a = {'a': 1,
          'b': 2,
          'c': (3, 4),
          }

print_a(**dict_a)

print_a(a=2, b=3, c=4)