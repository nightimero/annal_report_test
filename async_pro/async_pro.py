#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Topic: 协程
生产者-消费者实现
"""

#todo： https://www.xncoding.com/2015/12/21/python/nio.html
# todo： 深挖 yield 关键字
import time
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'
def producer(c):
    c.next()
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()
if __name__ == '__main__':
    c = consumer()
    producer(c)