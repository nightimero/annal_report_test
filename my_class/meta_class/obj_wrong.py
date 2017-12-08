# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser


class TextParser(HTMLParser):
    def __init__(self):
        super(TextParser, self).__init__()  # 可以这样修改
        # HTMLParser.__init__()
        self.all_data = []

# 查找资料之后发现，python中super只能应用于新类，而不能应用于经典类
# 所谓新类就是所有类都必须要有继承的类，如果什么都不想继承，就继承到object类。下面是一个新类的例子


TextParser()
