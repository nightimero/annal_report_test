# -*- coding:utf-8 -*-
from config import *
import random


#todo: 使用ipython运行程序，想运行示例中添加新的类的方法，使之生效。 简单的修改类是不行的。 %run Persona_case.py 是不行的的。
class Cases(object):
    def __init__(self,aidriver):
        self.aidriver = aidriver


    def case1(self):
        '''
        测试身高用例
        '''
        self.aidriver.send(random.choice([u'我是陈成', u'我叫陈成', u'我叫做陈成', u'我叫作陈成', u'我的名字是陈成', u'大家叫我陈成']))
        self.aidriver.check(u'陈成您好，请问有什么可以帮您？')
        self.aidriver.send(u'我的身高有1米6')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')
        self.aidriver.send(u'我有多高呢？')
        self.aidriver.checkin([u'我猜您身高应该是160厘米。',u'您身高160厘米。'])
        #修改身高
        self.aidriver.send(u'我的身高有1米7')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')
        self.aidriver.send(u'我有多高呢？')
        self.aidriver.checkin([u'我猜您身高应该是170厘米。', u'您身高170厘米。'])
        #多种问法
        self.aidriver.send(u'我有多高？')
        self.aidriver.checkin([u'我猜您身高应该是170厘米。', u'您身高170厘米。'])
        self.aidriver.send(u'我有身高有多少？')
        self.aidriver.checkin([u'我猜您身高应该是170厘米。', u'您身高170厘米。'])
        self.aidriver.send(u'你猜我身高是多少')
        self.aidriver.checkin([u'我猜您身高应该是170厘米。', u'您身高170厘米。'])
        self.aidriver.send(u'你猜我身高是多少')
        self.aidriver.checkin([u'我猜您身高应该是170厘米。', u'您身高170厘米。'])


    def case2(self):
        '''
        性别
        '''
        self.aidriver.send(random.choice([u'我是陈成', u'我叫陈成',u'我叫做陈成', u'我的名字是陈成', u'大家叫我陈成']))
        self.aidriver.check(u'陈成您好，请问有什么可以帮您？')
        self.aidriver.send(u'我的性别是什么？')
        self.aidriver.check(u'我还不知道呢，您能告诉我吗？')
        self.aidriver.send(u'是男的。')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')
        self.aidriver.send(u'我的性别是什么呢？')
        self.aidriver.check(u'先生您好，请问有什么可以帮您？')
        # 修改性别
        self.aidriver.send(u'我不是男的，是女的。')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')
        self.aidriver.send(u'我的性别是什么呢？')
        self.aidriver.check(u'女士您好，请问有什么可以帮您？')
        #多种问法
        self.aidriver.send(u'我是女性。')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')
        self.aidriver.send(u'我是女人。')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')

    def case3(self):
        '''
        年龄
        '''
        self.aidriver.send(random.choice([u'我是陈成', u'我叫陈成', u'我叫做陈成', u'我叫作陈成', u'我的名字是陈成', u'大家叫我陈成']))
        self.aidriver.check(u'陈成您好，请问有什么可以帮您？')
        self.aidriver.send(u'我今年多大了？')
        self.aidriver.checkin([u'这个我还不知道呢，要不您直接告诉我吧。',u'我掐指一算。。。'
                                                      u'算。。算。。。算。。。哎呀，大人真是天命，我实在是算不出来，要不您告诉我吧。',])
        self.aidriver.send(u'我16岁')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')
        self.aidriver.send(u'我今年多大了？')
        self.aidriver.checkin([u'我掐指一算，您今年应该16岁了。',u'您好，我猜您今年16岁了吧。',])
        #修改年龄
        self.aidriver.send(u'我今年19岁')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')
        self.aidriver.send(u'我今年多大了？')
        self.aidriver.checkin([u'我掐指一算，您今年应该19岁了。',u'您好，我猜您今年19岁了吧。',])
        #年龄多问法
        self.aidriver.send(u'我其实今年是18岁')
        self.aidriver.checkin([u'我知道了，请问有什么可以帮您？',])
        self.aidriver.send(u'你知道我的年龄吗？')
        self.aidriver.checkin([u'我掐指一算，您今年应该18岁了。', u'您好，我猜您今年18岁了吧。', ])
        self.aidriver.send(u'我九六年出生的')
        self.aidriver.checkin([u'我知道了，请问有什么可以帮您？',])
        self.aidriver.send(u'你知道我的年龄吗？')
        self.aidriver.checkin([u'我掐指一算，您今年应该21岁了。', u'您好，我猜您今年21岁了吧。', ])
        self.aidriver.send(u'我86年出生的')
        self.aidriver.checkin([u'我知道了，请问有什么可以帮您？',])
        self.aidriver.send(u'你知道我的年龄吗？')
        self.aidriver.checkin([u'我掐指一算，您今年应该31岁了。', u'您好，我猜您今年31岁了吧。', ])
        self.aidriver.send(u'我1996年出生的')
        self.aidriver.checkin([u'我知道了，请问有什么可以帮您？',])
        self.aidriver.send(u'你知道我的年龄吗？')
        self.aidriver.checkin([u'我掐指一算，您今年应该21岁了。', u'您好，我猜您今年21岁了吧。', ])


    def case4(self):
        '''
        体重
        '''
        self.aidriver.send(random.choice([u'我是陈成', u'我叫陈成', u'我叫做陈成', u'我叫作陈成', u'我的名字是陈成', u'大家叫我陈成']))
        self.aidriver.check(u'陈成您好，请问有什么可以帮您？')
        self.aidriver.send(u'你知道我体重多重吗？')
        self.aidriver.checkin([u'这个可难倒我了，你可以告诉我您的体重吗？',])
        self.aidriver.send(u'我体重160斤')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')
        self.aidriver.send(u'我的体重是多少？')
        self.aidriver.checkin([u'我记得您的体重应该是80kg',u'您的体重是80kg。'])
        #修改体重
        self.aidriver.send(u'我的体重是200斤')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')
        self.aidriver.send(u'我的体重是多少？')
        self.aidriver.checkin([u'我记得您的体重应该是100kg', u'您的体重是100kg。'])
        #体重多问法
        self.aidriver.send(u'我其实体重是180斤')
        self.aidriver.checkin([u'我知道了，请问有什么可以帮您？',])



    def case5(self):
        '''
        血型
        '''
        self.aidriver.send(random.choice([u'我是陈成', u'我叫陈成', u'我叫做陈成', u'我叫作陈成', u'我的名字是陈成', u'大家叫我陈成']))
        self.aidriver.check(u'陈成您好，请问有什么可以帮您？')
        self.aidriver.send(u'我的血型是什么？')
        self.aidriver.checkin([u'这个我还不知道呢，您能告诉我吗？',u'您还没告诉您是什么血型呢',u'我也想知道您是什么血型哦'])
        self.aidriver.send(u'我的血型是O型')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')
        self.aidriver.send(u'我的血型是什么？')
        self.aidriver.checkin([u'您的血型应该是O型血',u'您是O型血。',u'我记得您应该是O型血'])
        #修改血型
        self.aidriver.send(u'我的血型是ab型')
        self.aidriver.check(u'我知道了，请问有什么可以帮您？')
        self.aidriver.send(u'我的血型是什么？')
        self.aidriver.checkin([u'您的血型应该是AB型血', u'您是AB型血。', u'我记得您应该是AB型血'])
        #血型多问法
        self.aidriver.send(u'你知道我血型吗')
        self.aidriver.checkin([u'您的血型应该是AB型血', u'您是AB型血。', u'我记得您应该是AB型血'])


    def case6(self):
        '''
        一次性输入所有属性。
        '''
        self.aidriver.send(random.choice([u'我是陈成,性别男，我今年18岁，体重110斤，身高1米5，血型是AB型血型',]))
        self.aidriver.send(random.choice([u'我是谁',]))
        self.aidriver.check(u'陈成您好，请问有什么可以帮您？')
        self.aidriver.send(u'我的性别是什么？')
        self.aidriver.checkin([u'先生您好，请问有什么可以帮您？',])
        self.aidriver.send(u'我今年多大了？')
        self.aidriver.checkin([u'我掐指一算，您今年应该18岁了。', u'您好，我猜您今年18岁了吧。', ])
        self.aidriver.send(u'我有多高呢？')
        self.aidriver.checkin([u'我猜您身高应该是150厘米。',u'您身高150厘米。'])
        self.aidriver.send(u'我的体重是多少？')
        self.aidriver.checkin([u'我记得您的体重应该是55kg',u'您的体重是55kg。'])
        self.aidriver.send(u'我的血型是什么？')
        self.aidriver.checkin([u'您的血型应该是AB型血',u'您是AB型血。',u'我记得您应该是AB型血'])

# task: 打补丁  :result： 因为aichat和aichat.case中都包含self.aidriver，恰好使用aichat.cases.case10 = types.MethodType(case10,aichat)和
# aichat.cases.case10 = types.MethodType(case10,aichat.cases)都可以用。但是按照标准，其实很简单，方法在哪个类中，就传入哪个类的实例。
    # 所以这里应该是aichat.cases.case10 = types.MethodType(case10,aichat.cases)
    #这里绑定的是实例方法，不影响其他实例类。
    #应该要参考这个项目打补丁 http://python.jobbole.com/82357/
#TypeError: case7() takes exactly 1 argument (0 given)
#case7 在运行后添加，无法生效。aichat.cases.case7 = case7 。 估计打补丁的方式不对。
# aichat.cases.case17 = case17(AiChat().cases) 这样的方式也不可以。相当于运行了函数，返回结果。
    def case17(self):
        print 'test'

    def case26(self):
        '''
        一次性输入所有属性。
        '''
        self.aidriver.send(random.choice([u'我是陈成,性别男，我今年18岁，体重110斤，身高1米5，血型是AB型血型',]))
        self.aidriver.send(random.choice([u'我是谁',]))
        self.aidriver.check(u'陈成您好，请问有什么可以帮您？')
        self.aidriver.send(u'我的性别是什么？')
        self.aidriver.checkin([u'先生您好，请问有什么可以帮您？',])
        self.aidriver.send(u'我今年多大了？')
        self.aidriver.checkin([u'我掐指一算，您今年应该18岁了。', u'您好，我猜您今年18岁了吧。', ])
        self.aidriver.send(u'我有多高呢？')
        self.aidriver.checkin([u'我猜您身高应该是150厘米。',u'您身高150厘米。'])
        self.aidriver.send(u'我的体重是多少？')
        self.aidriver.checkin([u'我记得您的体重应该是55kg',u'您的体重是55kg。'])
        self.aidriver.send(u'我的血型是什么？')
        self.aidriver.checkin([u'您的血型应该是AB型血',u'您是AB型血。',u'我记得您应该是AB型血'])




    def case23(self):
        '''
        理财场景不对
        '''
        self.aidriver.send(u'我要理财')
        self.aidriver.send(u'3.00%')
        self.aidriver.send(u'1年')
        self.aidriver.send(u'五万')
        self.aidriver.check(u'2017年同心众盈网银专享保本型第24期\n3%\n年化收益率\n12个月\n理财期限\n点击查看详情')

