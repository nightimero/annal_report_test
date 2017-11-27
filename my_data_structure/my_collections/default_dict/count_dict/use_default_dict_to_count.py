# -*- coding:utf-8 -*-
# 默认值可以很方便
# 
# 众所周知，在Python中如果访问字典中不存在的键，会引发KeyError异常（JavaScript中如果对象中不存在某个属性，
# 则返回undefined）。但是有时候，字典中的每个键都存在默认值是非常方便的。例如下面的例子：

strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}

try:
    for kw in strings:
        counts[kw] += 1
except KeyError as e:
    print 'key error:', e
# 该例子统计strings中某个单词出现的次数，并在counts字典中作记录。
# 单词每出现一次，在counts相对应的键所存的值数字加1。但是事实上，运行这段代码会抛出KeyError异常，出现的时机是每个单词第一次统计的时候，因为Python的dict中不存在默认值的说法，可以在Python命令行中验证：

# counts = dict()
# counts['puppy'] += 1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'puppy'

# 使用判断语句检查

# 既然如此，首先可能想到的方法是在单词第一次统计的时候，在counts中相应的键存下默认值1。
# 这需要在处理的时候添加一个判断语句：

strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}

for kw in strings:
    if kw not in counts:
        counts[kw] = 1
    else:
        counts[kw] += 1

print counts
# {'puppy': 5, 'weasel': 1, 'kitten': 2}
