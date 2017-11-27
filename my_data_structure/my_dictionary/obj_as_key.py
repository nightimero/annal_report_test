# -*- coding:utf-8 -*-

# list_all = []
# dict_all = {}
# def add_to_list(list_single):
#     list_all.append(list_single)
#     dict_all[list_single] = list_single()
#     return list_single
#
# @add_to_list
# class A():
#     list_a = [1, 2]
#
# @add_to_list
# class B():
#     list_b = [3, 4]
#
# print type(dict_all.keys()[0])

# ================================================================================
# <type 'classobj'> 这里说明了，dict的key不一定是str。classobj也可以。
#但是实例不能作为直接作为dict的key。比如以下这段：
# class Obj():
#     def __init__(self, value):
#         self.value = value
#
# dct = {Obj(foo):foo_value, Obj(bar):bar_value}
# ================================================================================
#todo: https://stackoverflow.com/questions/45269944/python-from-a-dict-how-retrieve-object-as-key
#todo: https://www.google.com/search?q=python+dict+key+classobj&oq=python+dict+key+classobj
# __hash__ 和 __eq__ 有啥用？
class Obj():
    def __init__(self, name):
        self.name = name
    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
    def __repr__(self):
        return str(self.name)

dct = {Obj('item1'):1, Obj('item2'):2}

print(dct.keys())
# dct['item1']
#这样肯定不行啊。这里itme1是字符串，不是Obj('item1')对象

#提问者不是想要的这个
x = Obj("item1")
y = Obj("item2")
dct= {x:1, y:2}
print dct[x]

a = Obj(3)
print a


