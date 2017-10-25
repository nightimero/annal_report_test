# -*- coding:utf-8 -*-

dict_a = {'a': 2, 'b': 3}
dict_a_key_new = {}
dict_a_value_new = {}
# for key, value in enumerate(dict(dict_a)):   将dict再dict也是画蛇添足
for key, value in enumerate(dict_a):
    dict_a_key_new[key] = value
    print key, value

print dict_a_key_new

for key, value in enumerate(dict_a.values()):
    dict_a_value_new[key] = value
    print key, value

print dict_a_value_new
