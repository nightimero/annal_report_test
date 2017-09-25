# -*- coding:utf-8 -*-

list_all =[]
def add_to_list(list_single):
    list_all.append(list_single)
    return list_single

@add_to_list
class A():
    list_a = [1, 2]

@add_to_list
class B():
    list_b = [3, 4]

print list_all
print list_all[0].list_a