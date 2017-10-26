# -*- coding:utf-8 -*-
# 应用场景 - 页面点击数
#
# 　　《Redis Cookbook》对这个经典场景进行详细描述。假定我们对一系列页面需要记录点击次数。
# 例如论坛的每个帖子都要记录点击次数，而点击次数比回帖的次数的多得多。如果使用关系数据库来存储点击，
# 可能存在大量的行级锁争用。所以，点击数的增加使用redis的INCR命令最好不过了。
#
# 　　当redis服务器启动时，可以从关系数据库读入点击数的初始值（1237这个页面被访问了34634次）

import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
r.set('visit:1234:total', 34634)
print 'incr:', r.incr('visit:1234:total')
print 'get:', r.get('visit:1234:total')
