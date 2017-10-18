# -*- coding:utf-8 -*-
from django.db import models
# 究竟为什么要使用元类？
#
# 现在回到我们的大主题上来，究竟是为什么你会去使用这样一种容易出错且晦涩的特性？好吧，一般来说，你根本就用不上它：
#
# “元类就是深度的魔法，99%的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。
# 那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。”
# —— Python界的领袖 Tim Peters
#
# 元类的主要用途是创建API。一个典型的例子是Django ORM。它允许你像这样定义：


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
# 但是如果你像这样做的话：


guy = Person(name='bob', age='35')
print guy.age


guy = Person(name='bob', age='35')
print guy.age
# 这并不会返回一个IntegerField对象，而是会返回一个int，甚至可以直接从数据库中取出数据。
# 这是有可能的，因为models.Model定义了__metaclass__，
# 并且使用了一些魔法能够将你刚刚定义的简单的Person类转变成对数据库的一个复杂hook。
# Django框架将这些看起来很复杂的东西通过暴露出一个简单的使用元类的API将其化简，
# 通过这个API重新创建代码，在背后完成真正的工作。
