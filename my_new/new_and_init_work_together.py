# -*- coding:utf-8 -*-
# todo（2017-10-14 15:42:24 link to my_object）。 搜索 new super


class AA(object):
    """
    如果__new__返回一个对象的实例，会隐式调用__init__
    """
    def __new__(cls, *args, **kwargs):
        object_a = super(AA, cls).__new__(cls)
        print 'in new'
        print object_a  # 可以看出object_a是一个实例。<__main__.AA object at 0x0302A1F0>
        return object_a

    def __init__(self):
        print 'in init'

AA()


class BB(object):
    """
    如果__new__不返回一个对象的实例，__init__不会被调用
    """
    def __new__(cls, *args, **kwargs):
        print "in new_b"
        print cls   # 返回的不是实例 <class '__main__.BB'>
        return cls

    def __init__(self):
        print 'in init_b'

BB()
