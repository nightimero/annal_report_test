# -*- coding:utf-8 -*-
import re
import inspect

test2 = "hello world hello me"

# find是从左到右查找。 rfind是从右向左查找。 没有都返回一

print test2.find("hello")

print test2.rfind("hello")

print test2.find("hello", 1) # 从第一个字符索引开始

#  第二，还可以使用in判断是否包含字符串

print "hello" in test2

# 第三，通过index

print test2.index("hello")

# 如果要查询所有子字符串的索引呢？

# that's the goal
# print string.find_all('test') # [0,5,10,15]

#  只有使用正则表达式

# todo： map 和filter，map和filter加匿名函数如何使用？
#
# def findSubstrings(substrings,destString):
#     res =  map(lambda x:str([destString.index(x),x]),filter(lambda x:x in destString,substrings))
#     if res:
#         return ', '.join(list(res))

# # 等效于
# def findSubstrings(substrings,destString):
#     return ', '.join([str([destString.index(x),x]) for x in substrings if x in destString])

# finditer是个好东西啊。居然是iter callable
print [x.start() for x in re.finditer('test', 'test test test test')]
print "x.end:", [x.end() for x in re.finditer('test', 'test test test test')]
print "x.end with group:", [x.end(0) for x in re.finditer(r'test', 'test test test test')]
# todo: 区别正则中group，groups，groupdict

# todo： 然后了解这些函数
# 'end',
# 'endpos',
# 'expand',
# 'group',
# 'groupdict',
# 'groups',
# 'lastgroup',
# 'lastindex',
# 'pos',
# 're',
# 'regs',
# 'span',
# 'start',
# 'string'

print "x.group:", [x.group(0) for x in re.finditer('test\d', 'test test1 test2 test')]
print "x.groups:", [x.groups(2) for x in re.finditer('(test\d)', 'test test1 test2 test')]
print "dir all:", [dir(x) for x in re.finditer('test', 'test')]  # 查看到了可迭代对象的所有方法和属性

obj2 = re.finditer('test', 'test')
list2 = [dir(x) for x in obj2][0]  #
[dir(x) for x in obj2]  # todo: 还不好写。 查找callable-iterator对象中的方法。callable的。

print "re.finditer 的Type：", type(re.finditer('test', 'test'))
print "普通list的Type:", type([1, 2, 3,])  # <type 'list'>
# 打印可迭代对象的type：
# 生成一个可迭代对象。
class Fib:
    def __init__(self):
      self.prev=0
      self.curr=1
    def __iter__(self):
      return self
    def __next__(self):
        value=self.curr
        self.curr+=self.prev
        self.prev=value
        return value
print "Fib 的type：", type(Fib)  # <type 'classobj'>
print "Fib实例 的type：", type(Fib())  # <type 'instance'>


# 下面这样就错了。输出属性少了。为什么这样属性会少了呢？ in 后面的对象都不同。
# 一个是可迭代对象。一个是可迭代对象列表。
print "dir all dir after in:", [x for x in dir(re.finditer('test', 'test'))]
print "re.finditer的class:", re.finditer('test', 'test').__class__

# 下面这样写也不行。
# obj1 = re.finditer('test', 'test')
# print [x for x in dir(obj1) if callable(getattr(obj1, x))]

# # 下面这种写法是错误的。
# print [x for x in dir(re.finditer('test', 'test')) if callable(getattr(re.finditer('test', 'test'),x))]

print "x.string: ", [x.string for x in re.finditer('test', 'test test test')]
print "x.string: ", [x.string for x in re.finditer('test', 'test test test')]

# 使用__dict__是不行的。
# print [x.__dict__ for x in re.finditer('test', 'test')]  # 查看到了可迭代对象的所有方法和属性

print [x.span() for x in re.finditer('test', 'test test')]

# # TypeError: span() takes no keyword arguments
# print [x.span(group = 1) for x in re.finditer('test', 'test test')]
# 查看对象方法所需要的入参。
print "x.span with group:", [x.span(0) for x in re.finditer('test', 'test test')]

# raise TypeError('{!r} is not a Python function'.format(func))
# TypeError: <built-in method span of _sre.SRE_Match object at 0x0000000003716168> is not a Python function
# todo: built-in method 不能使用inspect 查看吗？ 估计是。
# print "inspect the x.span with group:", [inspect.getargspec(x.span) for x in re.finditer('test', 'test test')]

print dir(re.finditer('test', 'test test test test'))
print dir((re.finditer('test', 'test test test test')).__iter__)

# print [x.match() for x in re.finditer('test', 'test test test test')]

print [x.start() for x in re.finditer('test', 'test test test test')]
