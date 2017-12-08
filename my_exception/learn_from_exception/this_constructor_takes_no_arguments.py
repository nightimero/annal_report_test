# -*- coding: utf-8 -*-
# __init__(self,name)这个构造函数的左右下划线都是两个，我只用了一个，导致错误。


class Person:
    population = 0

    def _init__(self, name):
        # def __init__(self, name):
        self.name = name
        print ('Initializing %s' % self.name)
        Person.population += 1

    def sayHi(self):
        print ('hi，My name is %s.' % self.name)

    def howMany(self):
        if Person.population == 1:
            print ('I am the current population .')
        else:
            print ('We have  %d persons here ' % Person.population)


swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()
