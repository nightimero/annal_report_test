# -*- coding:utf-8 -*-
# 使用dict.setdefault()方法
#
# 也可以通过dict.setdefault()方法来设置默认值：

strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}

for kw in strings:
    counts.setdefault(kw, 0)
    counts[kw] += 1  # 原PPT中这里有一个笔误

print counts
# dict.setdefault()方法接收两个参数，第一个参数是健的名称，第二个参数是默认值。
# 假如字典中不存在给定的键，则返回参数中提供的默认值；反之，则返回字典中保存的值。
# 利用dict.setdefault()方法的返回值可以重写for循环中的代码，使其更加简洁：

strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = {}

for kw in strings:
    counts[kw] = counts.setdefault(kw, 0) + 1

print counts
