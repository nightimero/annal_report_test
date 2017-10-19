# -*- coding:utf-8 -*-
import re

#http://blog.csdn.net/business122/article/details/7541486
#为什么我们还需要类的方法操作，比如OBJ.FUNC，就是因为instangc.FUNC无法满足我们在高阶函数时的需求。
#而python又是可以函数编程的。所以这里我们需要用到set.union
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]

set(list1) | set(list2)
# set.union(list1, list2) #这样是错误的
set.union(set(list1), set(list2))
lists = reduce(set.union, map(set, [list1, list2, list3]))
print locals()
print locals().keys()
list_names = [x for x in locals().keys() if re.match(r'list\d+', x)]
print [locals()[list_name] for list_name in list_names]
print [locals()[list_name] for list_name in list_names if re.match(r'list\d+', list_name)]

# 这里少了一步，从str获取变量。从字典获取变量
lists2 = reduce(set.union, map(set, [x for x in locals().keys() if re.match(r'list\d+', x)]))
print lists2

lists3 = reduce(set.union, map(set, [locals()[list_name] for list_name in list_names]))
print lists3

lists4 = reduce(set.union, map(set, map(locals().get, list_names)))
print lists4

# 可以将[for in]换成map的写法  map是从字典获取item
print 'local,list name:', [locals()[list_name] for list_name in list_names]
print 'map locals:', map(locals().get, list_names)

# todo: 为什么这么打印
print 'lists2{}'.format(list2)  # list2[7, 4]
print 'lists2{}'.format(lists2)  # list2[7, 4]


# set 是可迭代对象吗？ 是可以迭代的。
for _ in lists:
    print _
