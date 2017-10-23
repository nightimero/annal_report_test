# -*- coding:utf-8 -*-
from collections import defaultdict

strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')
counts = defaultdict(lambda: 0)  # 使用lambda来定义简单的函数

for s in strings:
    counts[s] += 1


def zero():
    return 0
dd = defaultdict(zero)
print dd
dd = defaultdict(list)
print dd
dd['name'].append('luke')


# __missing__ 方法
class DefaultDict(dict):
    # 函数作为参数传入，还是挺有意思的。
    def __init__(self, default_factory=None, *a, **kw):
        dict.__init__(self, *a, **kw)
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        self[key] = value = self.default_factory()
        return value

ab = DefaultDict(zero, name='test', **{'world': 'shawn'})
print ab
print ab['age']
ab['age'] = 12
print ab['age']
