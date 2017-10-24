#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Topic: 协程
生产者-消费者实现
"""

# https://www.xncoding.com/2015/12/21/python/nio.html
# 使用函数().next启动迭代器。
# yield 前面是send入参，后面是返回值。
# task： 在工作机器 添加 .ingnore 插件，使用文件右键ignore 功能。
# todo： 一定要写出来。总结。as a teacher ，speecher 就是复习

# todo：https://www.google.com/search?q=python+yield&oq=python+yield+&aqs=chrome..69i57.5194j0j7&sourceid=chrome&ie=UTF-8
# todo： 深挖 yield 关键字
import time


def consumer():
    r = ''
    while True:
        n = yield r
        # 以下两句是可以不要的。
        # if not n:
        #     return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'
        
        
def producer(consum):
    consum.next()
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = consum.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    consum.close()
    
if __name__ == '__main__':
    c = consumer()
    producer(c)
