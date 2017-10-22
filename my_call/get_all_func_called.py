# -*- coding:utf-8 -*-
__author__ = 'shawn'

# 注意：模块名不包括.py后缀
imp_module = 'test_import_class'
imp_class = 'ClassA'

# 方式1：使用__import__()导入模块
# 导入指定模块，导入时会执行全局方法。
ip_module = __import__(imp_module)
# dir()查看模块属性
print(dir(ip_module))

# 使用getattr()获取imp_module的类
test_class = getattr(ip_module, imp_class)
# 动态加载类test_class生成类对象
cls_obj = test_class()
# 查看对象属性
print(dir(cls_obj))
for attr in dir(cls_obj):
    # 加载非__前缀的属性
    if attr[0] != '_':
        # 获取导入obj方法。
        class_attr_obj = getattr(cls_obj, attr)

        # 判断类属性是否为函数
        if hasattr(class_attr_obj, '__call__'):
            # 执行函数
            class_attr_obj()
        else:
            # 输出类属性值
            print(attr, ' type:', type(class_attr_obj), ' value:', class_attr_obj)
