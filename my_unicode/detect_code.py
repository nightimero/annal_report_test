# -*- coding: utf-8 -*-
import chardet
with open("test.csv","rb") as f:
    data = f.read()
    print(chardet.detect(data))

# 用二进制模式读取
# 【编码方式讲解】
# （1）ANSI编码
# 不同的国家和地区制定了不同的标准，由此产生了 GB2312, BIG5, JIS 等各自的编码标准。这些使用 2 个字节来代表一个字符的各种汉字延伸编码方式，
    # 称为 ANSI 编码。在简体中文系统下，ANSI 编码代表 GB2312 编码，在日文操作系统下，ANSI 编码代表 JIS 编码。 不同 ANSI 编码之间互不兼容，
    # 当信息在国际间交流时，无法将属于两种语言的文字，存储在同一段 ANSI 编码的文本中。 当然对于ANSI编码而言，0x00~0x7F之间的字符，
    # 依旧是1个字节代表1个字符。这一点是ASNI编码与Unicode编码之间最大也最明显的区别。例如上面演示的文件中英文字母和数字并没有出现乱码的情况。
# （2）Unicode编码
# Unicode（统一码、万国码、单一码）是一种在计算机上使用的字符编码。它为每种语言中的每个字符设定了统一并且唯一的二进制编码，
    # 以满足跨语言、跨平台进行文本转换、处理的要求。1990年开始研发，1994年正式公布。随着计算机工作能力的增强，Unicode也在面世以来的十多年里得到普及。
# Unicode是国际组织制定的可以容纳世界上所有文字和符号的字符编码方案。Unicode用数字0-0x10FFFF来映射这些字符，最多可以容纳1114112个字符
    # ，或者说有1114112个码位。码位就是可以分配给字符的数字。UTF-8、UTF-16、UTF-32都是将数字转换到程序数据的编码方案。
# （3）UTF-8编码
# UTF-8是UNICODE的一种变长字符编码又称万国码，由Ken Thompson于1992年创建。现在已经标准化为RFC 3629。UTF-8用1到6个字节编码UNICODE字符。
    # 用在网页上可以同一页面显示中文简体繁体及其它语言(如日文，韩文)。