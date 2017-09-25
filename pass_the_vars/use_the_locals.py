# -*- coding:utf-8 -*-


#todo: locals()的用处
mynum = 1000
mystr = 'Hello World!'
print "{mystr} New-style formatting is {mynum}x more fun!".format(**locals())

print locals()
print locals().keys()
print globals().keys()
print type(locals())

#format的用法
print u"{} is a fish".format('luke')
print u"{} is a fish,{} is a hero".format('luke','lisa')
print u"{1} is a fish,{0} is a hero".format('luke','lisa')
names = ('luke','lisa')
print u"{1} is a fish,{0} is a hero".format(*names)

names = ('luke','lisa','noone')
print u"{1} is a fish,{0} is a hero".format(*names)

print u"{fish} is a fish,{hero} is a hero".format(hero ='lisa',fish='luke')
print u"{fish} is a fish,{hero} is a hero".format(**{'hero':'lisa','fish':'luke'})
print u"{鱼} is a 鱼,{英雄} is a 英雄".format(**{u'英雄':'lisa',u'鱼':'luke'})

#names在第一个globals没有，在第一个globals出现后，出现names，在第二个globals中有。
print globals().keys()