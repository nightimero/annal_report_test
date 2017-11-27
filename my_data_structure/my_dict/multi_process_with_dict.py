# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from multiprocessing import Process, Manager


def print_b(**kwargs):
    print 'print_b', kwargs
    print 'print_b,a:', kwargs['a']


# def print_a(**kwargs):  # 多进程是不接收这样的参数的。
def print_a(kwargs):
    print kwargs['a']
    print kwargs['b']
    print kwargs['c']
    print_b(**kwargs)


if __name__ == '__main__':
    manage = Manager()
    dict_a = manage.dict()
    dict_a['a'] = 1
    dict_a['b'] = 2
    dict_a['c'] = 3

    # t1 = Process(target=print_a, args=(dict_a,))  # print_a() takes exactly 0 arguments (1 given)
    t1 = Process(target=print_a, args=(dict_a,))  # print_a() takes exactly 0 arguments (1 given)
    t1.start()
    t1.join()
