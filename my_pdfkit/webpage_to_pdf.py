# -*- coding:utf-8 -*-
# 参考： http://www.cnblogs.com/taceywong/p/5643978.html
import pdfkit

# pdfkit.from_url('http://www.baidu.com', 'out1.pdf')
#
# pdfkit.from_file('test.html', 'out2.pdf')
# todo: pdfkit.from_string 报错，为什么？ 直接使用 from_string是正确的。但是三句话一起就报错。
pdfkit.from_string('Hello!', 'out3.pdf')
