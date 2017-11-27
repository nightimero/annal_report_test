# -*- coding:utf-8 -*-

class logging(object):
    def __init__(self, level='INFO'):
        self.level = level


    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                level=self.level,
                func=func.__name__)
            func(*args, **kwargs)

        return wrapper


@logging(level='INFO')
def say(something):
    print "say {}!".format(something)

say('hi')
