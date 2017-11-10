# -*- coding:utf-8 -*-
import multiprocessing


def worker(d, key, value):
    d[key] = value

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [multiprocessing.Process(target=worker, args=(d, i, i*2))
             for i in range(10)
             ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print ('Results:' )
    for key, value in enumerate(dict(d)):  # 这个enumerate用的尴尬了啊。
        print("%s=%s" % (key, value))

    for key, value in d.items():
        print key, value
    # 这样只是把key取出来了。取得不是key,value
    dict_a = {'a': 2, 'b': 3}
    for key, value in enumerate(dict(dict_a)):
        print key, value
    # 0    a
    # 1    b
    # 不过学到了 可以这样新建一个enumerate 的字典。
