# -*- coding: utf-8 -*-
print(repr('u8字\x00符串'.decode('utf8', 'replace')))
print 'u8字\x00符串'.decode('utf8', 'replace')
print 'u8字\x00符串'.decode('utf8')

# 字符串前面加u会默认构造出Unicode的字符串
unicodeString = u'Unicode字符串'

# 字符串前面什么都不加会构造出默认编码（首行限定了现在的utf8）的字符串
utf8String = 'Utf-8字符串'

# 如果我们把他们转化成同样的编码方式就可以操作（例如相加）
print(repr(unicodeString + utf8String.decode('utf8')))
print(repr(unicodeString.encode('utf8') + utf8String))

# 但如果不转化，当然就会出现满世界的烤鸭二舅啦
# unicodeString + utf8String

# 这里拿写入文件举例

# 一般使用Unicode
with open('Unicode.txt', 'w') as f: f.write(u'Unicode测试')

# 或者使用接收二进制编码的命令
with open('Utf8.txt', 'wb') as f: f.write('Utf8测试')

# 你可以反过来做个测试，自然会报错
# 二进制的命令方便了在不知道怎么解码的情况下也能进行操作（写入文件）