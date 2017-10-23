# -*- coding:utf-8 -*-
from collections import OrderedDict,namedtuple
__author__ = 'shawn'

list_of_lists = [
                ['20010103', '0.9507', '0.9569', '0.9262', '0.9271'],
                ['20010104', '0.9271', '0.9515', '0.9269', '0.9507'],
                ['20010105', '0.9507', '0.9591', '0.9464', '0.9575'],
                ]

names = ['date', 'open', 'high', 'low', 'close']

# 第一种方法
ListOfNamedtuple = namedtuple('ListOfNamedtuple', names)
for _list in list_of_lists:
    named_list = ListOfNamedtuple._make(_list)
    print named_list
    print named_list._asdict()

# 第二种方法
ordered_dictionary = [OrderedDict(zip(names, subl)) for subl in list_of_lists]
print ordered_dictionary

# 复习和升华了dict(zip(name,iterable)) for iterable in big_iter
ordered_dictionary = [dict(zip(names, subl)) for subl in list_of_lists]
print ordered_dictionary
