# -*- coding:utf-8 -*-
list_a = [1, 2, 3, ]

tuple_a = ('list','test',)

result = ["{word}".format(word=words) for words in tuple_a]

print words

print result

print tuple_a

print list_a

# 这样有一个现象。tuple_a在生成器最后，等于最后列表或tuple中最后一个值。因为 。
# for tuple_a in tuple_a 中第一个tuple_a赋值的原因。
result = ["{word}".format(word=tuple_a) for tuple_a in tuple_a]
