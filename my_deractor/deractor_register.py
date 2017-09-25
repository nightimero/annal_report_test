# -*- coding:utf-8 -*-

list_all = []
dict_all = {}
def add_to_list(list_single):
    list_all.append(list_single)
    dict_all[list_single] = list_single()
    return list_single

@add_to_list
class A():
    list_a = [1, 2]

@add_to_list
class B():
    list_b = [3, 4]

print type(dict_all.keys()[0]) # <type 'classobj'> 这里说明了，dict的key不一定是str。classobj也可以。
#但是实例不能作为dict的key。比如以下这段：
# class Obj():
#     def __init__(self, value):
#         self.value = value
#
# dct = {Obj(foo):foo_value, Obj(bar):bar_value}

print list_all
print list_all[0].list_a