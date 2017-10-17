# -*- coding:utf-8 -*-
from types import MethodType


class Student(object):
    def __init__(self, name, score):
        self.__name = name  # '_Student__name'
        self.__score = score  # '_Student__score'

    def print_score(self):
        print '%s : %s' % (self.__name, self.__score)

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
            self.__score = score

aa = Student('aa_name', 99)
aa.print_score()


def set_age(self, age):
    self.age = age


aa.set_age = MethodType(set_age, aa, Student)
aa.set_age(15)


def print_score(self):
    print '%s : %s' % (self.__name, self.__score)
    print 'age : %s ' % self.age

aa.print_score = MethodType(print_score, aa, Student)

try:
    aa.print_score()
except AttributeError as e:
    print e.message


def print_score2(self):
    print '%s : %s' % (self._Student__name, self._Student__score)
    print 'age : %s ' % self.age

# 使用这种方法就可以绑定了内部变量了。否则在外部运行时内部变量已被重命名。
aa.print_score2 = MethodType(print_score2, aa, Student)
aa.print_score2()
