# -*- coding:utf-8 -*-
#x,y,z = ((1),(2),(3,4)) x = 1 ,y = 2, z=(3,4) 不符合要求，应该是x,y,z = ((1,),(2,),(3,4))，这样x,y,z都是元组
x, y, z = ((1), (2), (3, 4))  # IDE 也提示 ：remove redundant（多余的） parentheses（圆括号）
x, y, z = ((1,), (2,), (3, 4))  # 这样IDE没有错误提示