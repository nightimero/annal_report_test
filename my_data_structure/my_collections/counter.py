# -*- coding:utf-8 -*-
from collections import Counter


# 错误的写法。多打印了。
def main():
    line = 'abbba'
    mp = {}

    for i in range(len(line)):
        if line[i] in mp:
            mp[line[i]] += 1
        else:
            mp[line[i]] = 1

    for i in range(len(line)):
        print line[i], ': ', mp[line[i]]


main()

print Counter('abbba')  # Counter({'b': 3, 'a': 2})
counts = Counter('abbba')
print counts['a']
print counts['b']

for k, v in Counter('abbba').iteritems():
    print k, v
