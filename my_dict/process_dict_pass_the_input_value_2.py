# -*- coding:utf-8 -*-
from multiprocessing import Process, Manager


def print_b(**kwargs):
    print 'print_b', kwargs
    print 'print_b,a:', kwargs['a']


def print_a(kwargs):
    print kwargs['a']
    print kwargs['b']
    print kwargs['c']
    kwargs['d'][1] = 7
    kwargs['e'] = 7
    print kwargs['d']
    # print_b(**kwargs)

if __name__ == '__main__':
    manager = Manager()
    dict_a = manager.dict()
    dict_a['a'] = 1
    dict_a['b'] = 2
    dict_a['c'] = (3, 4)
    dict_a['d'] = [3, 4]
    t1 = Process(target=print_a, args=(dict_a,))
    t1.start()
    t1.join()
    print dict_a['d']
    print dict_a['e']
