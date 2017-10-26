# -*- coding:utf-8 -*-
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.sadd('circle:game:lol', 'user:luke')
r.sadd('circle:game:lol', 'user:chen')
r.sadd('circle:game:lol', 'user:zhang')
r.sadd('circle:soccer:ACmilan', 'user:zhang')
r.sadd('circle:soccer:ACmilan', 'user:guo')
r.sadd('circle:soccer:ACmilan', 'user:zhao')
print 'r.smembers:', r.smembers('circle:game:lol')
print 'user like lol and ACmilan:', r.sinter('circle:game:lol', 'circle:soccer:ACmilan')
print 'user like lol or ACmilan:', r.sunion('circle:game:lol', 'circle:soccer:ACmilan')

