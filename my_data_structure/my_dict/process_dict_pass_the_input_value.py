# -*- coding:utf-8 -*-
from multiprocessing import Process


def print_b(**kwargs):
    print 'print_b', kwargs
    print 'print_b,a:', kwargs['a']


def print_a(**kwargs):
    print kwargs['a']
    print kwargs['b']
    print kwargs['c']
    kwargs['e'] = 7
    b_kwargs = kwargs
    kwargs['d'][1] = 7
    print_b(**b_kwargs)

if __name__ == '__main__':
    dict_a ={}
    dict_a['a'] = 1
    dict_a['b'] = 2
    dict_a['c'] = (3, 4)
    dict_a['d'] = [3, 4]
    t1 = Process(target=print_a, kwargs=dict_a)
    t1.start()
    t1.join()
    print dict_a['d']
