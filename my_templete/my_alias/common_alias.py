# -*- coding:utf-8 -*-
__author__ = 'shawn'

# 导入模块时，也可以给模块起别名，这样，可以在运行时根据当前环境选择最合适的模块
# Python标准库提供StringIO 和cStringIO 两个库，这两个库的接口和功能是一样的，但是cStringIO 是C写的，速度更快
# 优先导入cStringIO 。如果有些平台不提供cStringIO ，还可以降级使用StringIO
try:
    import cStringIO as StringIO
except ImportError:  # 如果导入失败,会捕获到ImportError
    import StringIO
# 导入cStringIO时，用import ... as ... 指定了别名StringIO ，因此，后续代码引用StringIO即可正常工作
# 类似的有simplejson库，在Python 2.6之前是独立的第三方库，从2.6开始内置成json
try:
    import json  # python >= 2.6
except ImportError:
    import simplejson as json  # python <= 2.5

# 小结：由于Python是动态语言，函数签名一致接口就一样，
# 因此，无论导入哪个模块后续代码都能正常工作，相对来说更安全
