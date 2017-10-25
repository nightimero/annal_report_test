# -*- coding:utf-8 -*-
# 这样就可以在linux和windows系统中通用了。
from multiprocessing import Process, Value, Array, Manager
from ctypes import c_char_p


def f(n, s, a, b, d):
    n.value = 3.1415927
    s.value = s.value + u'hello tester测试'
    for i in range(len(a)):
        a[i] = -a[i]
    for j in range(len(b)):
        print b[j]
    for k, v in d.items():  # 使用iteritems是错误的。
        print k, v
    for key in d.keys():
        print key

if __name__ == '__main__':
    num = Value('d', 0.0)  # 第二个参数必须是float
    manager = Manager()
    str1 = manager.Value(c_char_p, u'测试hello world')
    arr = Array('i', range(10))
    arr_str = manager.list([u'测试aa', u'world世界'])  # 不用Manage不行arr_str = Array(c_char_p, ['aa', 'world'])
    dict1 = manager.dict({'a': 1, 'b': 2})
    print 'arr_str:', arr_str[:]
    p = Process(target=f, args=(num, str1, arr, arr_str, dict1))
    p.start()
    p.join()

    print num.value
    print str1.value
    print arr[:]
