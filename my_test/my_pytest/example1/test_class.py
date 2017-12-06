# -*- coding: utf-8 -*-


class TestClass:
    # cannot collect test class 'TestClass' because it has a __init__ constructor
    # 不能添加__init__
    # def __init__(self):
    #     pass

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

# python -m pytest test_class.py
# python -m pytest -v test_class.py
# python -m pytest -q test_class.py

# 如何编写pytest测试样例
# 通过上面2个实例，我们发现编写pytest测试样例非常简单，只需要按照下面的规则：
# 测试文件以test_开头（以_test结尾也可以）
# 测试类以Test开头，并且不能带有 __init__ 方法
# 测试函数以test_开头
# 断言使用基本的assert即可


# py.test               # run all tests below current dir
# py.test test_mod.py   # run tests in module
# py.test somepath      # run all tests below somepath
# py.test -k stringexpr # only run tests with names that match the
#                       the "string expression", e.g. "MyClass and not method"
#                       will select TestMyClass.test_something
#                       but not TestMyClass.test_method_simple
# py.test test_mod.py::test_func # only run tests that match the "node ID",
                   # e.g "test_mod.py::test_func" will select
                               # only test_func in test_mod.py


# py.test -v test_class.py::TestClass
# py.test -v test_class.py::TestClass:test_one


# 生成HTML格式报告：

#  py.test --html=./report.html

# 生成XML格式的报告：

# py.test --junitxml=path   主要是为了方便Jenkin或其它的持续集成工具俱读取。


# 生成文本格式报告：
# py.test --resultlog=./log.txt