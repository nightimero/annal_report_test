# -*- coding:utf-8 -*-

class Ab(object):
    a = ['a', 'b']
    b = ['c', 'd']
    c = ['e', 'f']

    def method_a(self):
        pass

    # 获取全部locals
    def get_locals(self):
        print dir(self)

    # 获取方法(包括自己)
    def get_all_methods(self):
        print [func for func in dir(self) if callable(getattr(self, func))]

    # 获取方法(包括自己,只包括用户自定义方法)
    def get_all_methods(self):
        # todo:这里使用inspct模块来重写
        print [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")]
        print self.__dict__   # {'xyz': 123} 居然__dict__只返回了外部自定义的东东。

    # 获取方法(除却自己,只包括用户自定义方法)
    def get_all_methods(self):
        # 这里使用inspct模块来重写
        # 这里 not func == 'get_all_methods' 好丑陋，可以怎样重写。想self一样指代自己的方法。
        print [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__") and not func == 'get_all_methods']

    # 获取所有属性
    def get_all_attr(self):
        print [func for func in dir(self) if not callable(getattr(self, func))]

    # 获取所有属性(不包括系统变量)
    def get_all_attr(self):
        print [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    # 获取所有属性的引用
    def get_all_attr(self):
        print [getattr(self, attr) for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    # 获取所有属性加起来的引用
    def get_all_attr_add_to_one(self):
        print reduce(lambda x, y: x+y, [getattr(self, attr) for attr in dir(self)
                                        if not callable(getattr(self, attr)) and not attr.startswith("__")])


ab = Ab()
ab.get_all_attr()
ab.get_all_attr_add_to_one()
ab.xxx = ['ff', 'gg']
ab.get_all_attr_add_to_one()

ab.xyz = 123
ab.get_locals()
ab.get_all_methods()


