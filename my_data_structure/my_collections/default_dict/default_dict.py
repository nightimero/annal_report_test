# -*- coding:utf-8 -*-
from collections import defaultdict
counts = defaultdict(int)
for c in 'abbba':
    counts[c] += 1

print counts  # defaultdict(<type 'int'>, {'a': 2, 'b': 3})

mapping = {'some': 2, 'example': 3, 'words': 5}
for key in sorted(mapping.keys()):
    print key, mapping[key]
# example 3
# some 2
# words 5

