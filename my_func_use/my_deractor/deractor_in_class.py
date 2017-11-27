# -*- coding:utf-8 -*-
# TODO: https://segmentfault.com/a/1190000007321935


class AA(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):  # 接受函数
        def wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                level=self.level,
                func=func.__name__)
            func(*args, **kwargs)
        return wrapper  # 返回函数


@AA(level='INFO')
def say(something):
    print "say {}!".format(something)

say('hello world')


class BB(AA):
    @AA(level='INFO')
    def say(self):
        print 'hello tester'


class CC(AA):
    @AA(level='WARNING')
    def say(self):
        print 'hello tester'


class DD(AA):
    @AA(level='ERROR')
    def say(self):
        print 'hello tester'

bb = BB()
bb.say()
