# -*- coding:utf-8 -*-
# unicode
# 嗯，这也是一个 Python 的内置函数。函数签名如下：


# unicode(object='')
# unicode(object[, encoding[, errors]])

# 我想要讲还是 unicode 的可选参数 errors 。
#
# errors 这个可选参数有三个值 strict 、 ignore 、 replace
#
# 当我们用 unicode 函数将一个对象转换成 unicode 字符串时，如果遇到无法解析的字符，unicode 就会根据 errors 的值来决定如何处理该异常。
#
# strict
#
# 默认的行为，直接抛出 ValueError
# ingore
#
# 忽略无法解析的字符，并继续解析
# replace
#
# 用 U+FFFD 来代替该字符，并继续解析
# Tip
#
# 一个字符串的 decode 方法和 encode 方法也支持 errors 参数。

# todo: 如何模拟这个情况。使用error参数
str1 = {'name': 'luke', 'sex': u'男'}
print str1
print unicode(str1)
