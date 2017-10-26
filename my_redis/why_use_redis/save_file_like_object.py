# -*- coding:utf-8 -*-
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.hset('user:luke', 'name', 'luke')
r.hset('user:luke', 'email', 'nightimero2@163.com')
r.hset('user:luke', 'phone', '15828915224')
r.hset('user:luke', 'visit', '1')
print 'r.getall:', r.hgetall('user:luke')
print 'r.hkeys:', r.hkeys('user:luke')

