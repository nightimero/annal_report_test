# -*- coding:utf-8 -*-
from datetime import date
__author__ = 'shawn'
# random Person


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)
        # 这里理解为 Person(name,age)就可以了。

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.from_birth_year('John',  1986)
person1.display()
