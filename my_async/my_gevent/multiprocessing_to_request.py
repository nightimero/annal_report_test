# -*- coding:utf-8 -*-
from multiprocessing import Pool
import urllib2
import time


def f(url):
    print 'GET url:{}'.format(url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print '%d bytes received from %s.' % (len(data), url)

if __name__ =="__main__":
    s = time.time()
    pool = Pool(4)
    urls = [
    'http://www.baidu.com',
    'http://www.163.com',
    'http://www.qq.com',
    'http://www.sina.com',
    ]
    for url in urls:
        pool.apply_async(f, args=(url,))
    pool.close()
    pool.join()
    e = time.time()
    print u'cost time',e-s