# -*- coding:utf-8 -*-
Str = "this is string example....wow!!!"
Str = Str.encode('base64', 'strict')

print "Encoded String: " + Str
print "Decoded String: " + Str.decode('base64', 'strict')

# str  -> decode('the_coding_of_str') -> unicode
# unicode -> encode('the_coding_you_want') -> str
# http://blog.csdn.net/ktb2007/article/details/3876436
# http://blog.csdn.net/ktb2007/article/details/3876429