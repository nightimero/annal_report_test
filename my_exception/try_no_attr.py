# -*- coding:utf-8 -*-
# 再比如，当我们需要访问一个不确定的属性时，有可能你会写出这样的代码：


class A(object):
    pass


try:
    test = A()
    name = test.name  # not sure if we can get its name
except AttributeError:
    name = 'default'
    print name
# 其实你可以使用更简单的getattr()来达到你的目的。

name = getattr(test, 'name', 'default')
print name

# 最佳实践
# 最佳实践不限于编程语言，只是一些规则和填坑后的收获。
#
# 只处理你知道的异常，避免捕获所有异常然后吞掉它们。
# 抛出的异常应该说明原因，有时候你知道异常类型也猜不出所以然。
# 避免在catch语句块中干一些没意义的事情，捕获异常也是需要成本的。
# 不要使用异常来控制流程，那样你的程序会无比难懂和难维护。
# 如果有需要，切记使用finally来释放资源。
# 如果有需要，请不要忘记在处理异常后做清理工作或者回滚操作。
