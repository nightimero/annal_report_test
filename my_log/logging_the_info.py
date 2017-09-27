# -*- coding:utf-8 -*-
import logging

logging.info('test')
test =[u'\u597d\u7684\uff0c\u6211\u6e05\u695a\u4e86\uff0c\u6709\u4ec0\u4e48\u53ef\u4ee5\u5e2e\u60a8\u7684\u5462\uff1f']
logging.warning(repr([x.encode('utf-8') for x in test]).decode('string_escape'))