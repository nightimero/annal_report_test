# -*- coding:utf-8 -*-


class Person1(object):
    """Silly Person1"""

    def __new__(cls, name, age):
        print '__new__1 called.'
        # IDE 提示 unexpected argument
        # return super(Person1, cls).__new__(cls, name, age)
        return super(Person1, cls).__new__(cls)

    def __init__(self, name, age):
        print '__init__1 called.'
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person1: %s(%s)>' % (self.name, self.age)

piglei = Person1('piglei', 24)
print piglei


class Person2(object):
    """Silly Person2"""

    def __new__(cls):
        print '__new__2 called.'  # __new__2 没有被调用
        return super(Person2, cls).__new__(cls)

    def __init__(self, name, age):
        print '__init__2 called.'
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person2: %s(%s)>' % (self.name, self.age)
try:
    piglei = Person2('piglei', 24)
    print piglei
except TypeError as e:
    print e.message  # TypeError: __new__() takes exactly 1 argument (3 given)


class Person3(object):
    """Silly Person3"""

    def __new__(cls, name, age):
        print '__new__3 called.'  # __new__3 被调用
        return super(Person3, cls).__new__(cls, name, age)

    def __init__(self):
        print '__init__3 called.'

    # def __str__(self):
    #     return '<Person3: %s(%s)>' % (self.name, self.age)

try:
    piglei = Person3('piglei', 24)
    print piglei
except TypeError as e:
    print e.message  # TypeError: __init__() takes exactly 1 argument (3 given)
