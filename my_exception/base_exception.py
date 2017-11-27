# -*- coding:utf-8 -*-
# Exception 和 BaseException
# 当我们要捕获一个通用异常时，应该用Exception还是BaseException？我建议你还是看一下 官方文档说明，这两个异常到底有啥区别呢？ 请看它们之间的继承关系。
#
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration...
#       +-- StandardError...
#       +-- Warning...
# 从Exception的层级结构来看，BaseException是最基础的异常类，Exception继承了它。BaseException除了包含所有的Exception外还包含了SystemExit，KeyboardInterrupt和GeneratorExit三个异常。
#
# 由此看来你的程序在捕获所有异常时更应该使用Exception而不是BaseException，因为被排除的三个异常属于更高级别的异常，合理的做法应该是交给Python的解释器处理。
