# -*- coding:utf-8 -*-
# 所谓函数签名。
# 一个函数由这么几部分组成，函数名、参数个数、参数类型、返回值，函数签名由参数个数与其类型组成。
# 函数在重载时，利用函数签名的不同（即参数个数与类型的不同）来区别调用者到底调用的是那个方法！

# 函数type f(type1 arg1, type2 arg2)的签名就是type(type1, type2)，当然签名里还包括CV qualifier，但不包括storage class。
# 签名相同的函数指针具有相同类型。