# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
import nose
from nose.tools import set_trace


class TestAdd(unittest.TestCase):
    test_list = [
        ("name01", 1, 1, 2),
        ("name02", 2, 3, 5),
        ("name03", 3, 3, 6),
    ]

    # @parameterized.expand(test_list)
    # def test_add(self, name, a, b, c):
    #     self.assertEqual(a + b, c)

    @set_trace()   # todo: 如何调试  https://www.ibm.com/developerworks/cn/linux/l-cn-pythondebugger/index.html
    def test_add(self):
        self.assertEqual(3+5, 8)

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    # nose.main(defaultTest=__name__)
    # nose.run(argv=["", __file__, '--with-doctest', '-vv'])  # 这样可以
    # nose.run(argv=[TestAdd, "", '--with-doctest', '-vv'])  # 这样不行
    nose.runmodule(argv = ['-s', '-v'])   # 可以的
    # nose.run()   # 不行。
    # nose.runmodule(argv=['-v'])   # 可以的
    # nose.run(defaultTest=__name__)
    # --with-xunit 输出xml结果报告：

    # 查看要执行的用例列表：nosetests - -collect - only - v
