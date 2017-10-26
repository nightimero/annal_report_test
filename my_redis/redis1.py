# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
print 'set:', r.set('guo', 'shuai2')
print 'get:', r.get('guo')
print 'keys:', r.keys()
print 'dbsize:', r.dbsize()
print 'delete:', r.delete('guo')
print 'keys:', r.keys()
