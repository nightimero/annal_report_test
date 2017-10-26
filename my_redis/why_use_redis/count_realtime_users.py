# -*- coding:utf-8 -*-
# todo: http://www.cnblogs.com/clover-siyecao/p/5600078.html
# todo: http://debugo.com/python-redis/
# todo: http://flask.pocoo.org/snippets/71/
# todo: https://www.google.com/search?q=python+redis+应用  以后需要搜索加上 应用 2字，更实例。
import time
from redis import Redis
from datetime import datetime
ONLINE_LAST_MINUTES = 5
redis = Redis()


def mark_online(user_id):         # 将一个用户标记为online
    now = int(time.time())        # 当前的UNIX时间戳
    expires = now + (app.config['ONLINE_LAST_MINUTES'] * 60) + 10    # 过期的UNIX时间戳
    all_users_key = 'online-users/%d' % (now // 60)        # 集合名，包含分钟信息
    user_key = 'user-activity/%s' % user_id
    p = redis.pipeline()
    p.sadd(all_users_key, user_id)                         # 将用户id插入到包含分钟信息的集合中
    p.set(user_key, now)                                   # 记录用户的标记时间
    p.expireat(all_users_key, expires)                     # 设定集合的过期时间为UNIX的时间戳
    p.expireat(user_key, expires)
    p.execute()


def get_user_last_activity(user_id):        # 获得用户的最后活跃时间
    last_active = redis.get('user-activity/%s' % user_id)  # 如果获取不到，则返回None
    if last_active is None:
        return None
    return datetime.utcfromtimestamp(int(last_active))


def get_online_users():                     # 获得当前online用户的列表
    current = int(time.time()) // 60
    minutes = xrange(app.config['ONLINE_LAST_MINUTES'])
    return redis.sunion(['online-users/%d' % (current - x)        # 取ONLINE_LAST_MINUTES分钟对应集合的交集
                         for x in minutes])
