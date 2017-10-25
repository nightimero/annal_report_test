# -*- coding:utf-8 -*-
# todo: manager.Namespace()  可以引申到其他Namespace？
# 上面为manager.dict的使用实例。
#
#
#
# 2）namespace对象没有公共的方法，但是有可写的属性。
#
# 然而当使用manager返回的namespace的proxy的时候，_属性值属于proxy，跟原来的namespace没有关系。
# >> > manager = multiprocessing.Manager()
# >> > Global = manager.Namespace()
# >> > Global.x = 10
# >> > Global.y = 'hello'
# >> > Global._z = 12.3  # this is an attribute of the proxy
# >> > print(Global)
# Namespace(x=10, y='hello')
