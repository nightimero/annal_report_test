# -*- coding:utf-8 -*-
from gevent import monkey
monkey.patch_socket()
import gevent
import urllib2


def f(url):
    print 'GET url:{}'.format(url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print '%d bytes received from %s.' % (len(data), url)

gevent.joinall([
    gevent.spawn(f, 'http://www.baidu.com'),
    gevent.spawn(f, 'http://www.163.com'),
    gevent.spawn(f, 'http://www.sina.com'),
    gevent.spawn(f, 'http://www.qq.com'),
])
