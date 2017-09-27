# -*- coding:utf-8 -*-
from config import *
import random


#todo: 使用ipython运行程序，想运行示例中添加新的类的方法，使之生效。 简单的修改类是不行的。 %run Persona_case.py 是不行的的。
class Cases(object):
    def __init__(self,aidriver):
        self.aidriver = aidriver

# ===================================================冒烟测试用例=================================================
    def case1(self):
        '''
        测试身高用例
        '''
        self.aidriver.send(random.choice([u'我是陈成', u'我叫陈成', u'我叫做陈成', u'我叫作陈成', u'我的名字是陈成', u'大家叫我陈成']))
        self.aidriver.check(u'好的，我知道了,有什么可以帮您的呢？')
        self.aidriver.send(u'我的身高有1米6')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我有多高呢？')
        self.aidriver.checkin([u'我猜您身高应该是160厘米。',u'您身高160厘米。'])
        #修改身高
        self.aidriver.send(u'我的身高有1米7')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
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
        self.aidriver.send(random.choice([u'我是陈成', u'我叫陈成', u'我叫做陈成', u'我的名字是陈成', u'大家叫我陈成']))
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？', u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我的性别是什么？')
        self.aidriver.check(u'我还不知道呢，您能告诉我吗？')
        self.aidriver.send(u'是男的。')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我的性别是什么呢？')
        self.aidriver.checkin([u'先生您好，请问有什么可以帮您？', u'您性别是男，请问有什么可以帮您？'])
        # 修改性别
        self.aidriver.send(u'我不是男的，是女的。')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我的性别是什么呢？')
        self.aidriver.checkin([u'女士您好，请问有什么可以帮您？', u'您性别是女，请问有什么可以帮您？'])
        # 多种问法
        self.aidriver.send(u'我是女性。')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我是女人。')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我是男是女。')
        self.aidriver.checkin([u'女士您好，请问有什么可以帮您？', u'您性别是女，请问有什么可以帮您？'])
        self.aidriver.send(u'我是女的么。')
        self.aidriver.checkin([u'女士您好，请问有什么可以帮您？', u'您性别是女，请问有什么可以帮您？'])

    def case3(self):
        '''
        年龄
        '''
        self.aidriver.send(random.choice([u'我是陈成', u'我叫陈成', u'我叫做陈成', u'我叫作陈成', u'我的名字是陈成', u'大家叫我陈成']))
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我今年多大了？')
        self.aidriver.checkin([u'这个我还不知道呢，要不您直接告诉我吧。',
                               u'我掐指一算。。。算。。算。。。算。。。哎呀，大人真是天命，'
                               u'我实在是算不出来，要不您告诉我吧。',
                               u'我还不太清楚您的年龄呢，你能告诉我吗？',])
        self.aidriver.send(u'我16岁')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我今年多大了？')
        self.aidriver.checkin([u'我掐指一算，您今年应该16岁了。',u'您好，我猜您今年16岁了吧。',])
        #修改年龄
        self.aidriver.send(u'我今年19岁')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我今年多大了？')
        self.aidriver.checkin([u'我掐指一算，您今年应该19岁了。',u'您好，我猜您今年19岁了吧。',])
        #年龄多问法
        self.aidriver.send(u'我其实今年是18岁')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',])
        self.aidriver.send(u'你知道我的年龄吗？')
        self.aidriver.checkin([u'我掐指一算，您今年应该18岁了。', u'您好，我猜您今年18岁了吧。', ])
        self.aidriver.send(u'我九六年出生的')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',])
        self.aidriver.send(u'你知道我的年龄吗？')
        self.aidriver.checkin([u'我掐指一算，您今年应该21岁了。', u'您好，我猜您今年21岁了吧。', ])
        self.aidriver.send(u'我86年出生的')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',])
        self.aidriver.send(u'你知道我的年龄吗？')
        self.aidriver.checkin([u'我掐指一算，您今年应该31岁了。', u'您好，我猜您今年31岁了吧。', ])
        self.aidriver.send(u'我1996年出生的')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',])
        self.aidriver.send(u'你知道我的年龄吗？')
        self.aidriver.checkin([u'我掐指一算，您今年应该21岁了。', u'您好，我猜您今年21岁了吧。', ])


    def case4(self):
        '''
        体重
        '''
        self.aidriver.send(random.choice([u'我是陈成', u'我叫陈成', u'我叫做陈成', u'我叫作陈成', u'我的名字是陈成', u'大家叫我陈成']))
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'你知道我体重多重吗？')
        self.aidriver.checkin([u'这个可难倒我了，你可以告诉我您的体重吗？',])
        self.aidriver.send(u'我体重160斤')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我的体重是多少？')
        self.aidriver.checkin([u'我记得您的体重应该是80kg',u'您的体重是80kg。'])
        #修改体重
        self.aidriver.send(u'我的体重是200斤')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我的体重是多少？')
        self.aidriver.checkin([u'我记得您的体重应该是100kg', u'您的体重是100kg。'])
        #体重多问法
        self.aidriver.send(u'我其实体重是180斤')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',])



    def case5(self):
        '''
        血型
        '''
        self.aidriver.send(random.choice([u'我是陈成', u'我叫陈成', u'我叫做陈成', u'我叫作陈成', u'我的名字是陈成', u'大家叫我陈成']))
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我的血型是什么？')
        self.aidriver.checkin([u'这个我还不知道呢，您能告诉我吗？',u'您还没告诉您是什么血型呢',u'我也想知道您是什么血型哦'])
        self.aidriver.send(u'我的血型是O型')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
        self.aidriver.send(u'我的血型是什么？')
        self.aidriver.checkin([u'您的血型应该是O型血',u'您是O型血。',u'我记得您应该是O型血'])
        #修改血型
        self.aidriver.send(u'我的血型是ab型')
        self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？',u'好的，我知道了,有什么可以帮您的呢？'])
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
        self.aidriver.checkin([u'您叫陈成,请问有什么可以帮您？',])
        self.aidriver.send(u'我的性别是什么？')
        self.aidriver.checkin([u'您性别是男，请问有什么可以帮您？',])
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

    #
    # import types
    #
    # class Person(object):
    #     pass
    #
    # def say(self):
    #     print 'hello, world'
    #
    # p = Person()
    # 应该是写作 p.say = types.MethodType(say, p, Person)  Person 是不必要的参数，因为函数只需两个参数，所以传入了，没有报错正常执行。
    # p.say = types.MethodType(say, p, Person)
    # p.say()
    #

#===================================================冒烟测试用例=================================================

    def case7(self):
        '''
        姓名 - 多问法进入姓名测试
        '''

        who_i_ams = []
        who_i_am_1 = [u'我叫%s'%x for x in (u'什么',u'啥',)]
        who_i_am_2 = [u'我是谁']
        #x,y,z = ((1),(2),(3,4)) x = 1 ,y = 2, z=(3,4) 不符合要求，应该是x,y,z = ((1,),(2,),(3,4))，这样x,y,z都是元组
        who_i_am_3 = [u'我{0}{1}是{2}'.format(x,y,z) for x in (u'的',u'',) for y in (u'名字',u'姓名',) for z in (u'什么',u'啥',)]
        who_i_am_4 = [u'{}我{}{}'.format(x,y,z) for x in (u'请问',u'你知道',) for y in (u'的',u'',) for z in (u'名字',u'姓名',)]
        who_i_am_5 = [u'我{}{}'.format(x,y) for x in (u'的',u'',) for y in (u'名字',u'姓名',)]
        who_i_am_6 = [u'{}呢'.format(x) for x in (u'名字',u'姓名',)]
        who_i_ams = who_i_am_1 + who_i_am_2 + who_i_am_3 + who_i_am_4 + who_i_am_5 + who_i_am_6

        for who_i_am in who_i_ams:
            self.aidriver.open_chat_page()
            self.aidriver.send(who_i_am)
            self.aidriver.checkin([u'我也想知道您叫什么名字', u'我还不知道呢，您能告诉我吗？',
                                   u'您还没告诉我您的名字呢',u'这个我还不知道呢，您能告诉我吗？', ])
            self.aidriver.driver.delete_all_cookies()

    def case8(self):
        '''
        姓名 - 多问法回答名字
        '''

        my_name_iss = []
        names = (u'高登科',u'王小丫',)
        my_name_is_1 = [u'我{0}{name}'.format(x,name=name) for x in (u'是',u'叫做',u'叫作',u'叫',) for name in names]
        my_name_is_2 = [u'我{0}{1}{2}{name}'.format(x,y,z,name=name) for x in (u'的',u'',) for y in (u'名字',u'姓名',)
                        for z in (u'是',u'叫',u'叫做',u'叫作',u'为',)  for name in names]
        my_name_is_3 = [u'大家{0}我{name}'.format(x,name=name) for x in (u'叫',u'喊',u'称',)  for name in names]
        my_name_is_4 = [u'{name}'.format(name=name) for name in names]
        my_name_iss = my_name_is_1 + my_name_is_2 + my_name_is_3 + my_name_is_4

        for my_name_is in my_name_iss:
            self.aidriver.open_chat_page()
            self.aidriver.send(u'我是谁')
            self.aidriver.send(my_name_is)
            self.aidriver.checkin([u'好的，我知道了,有什么可以帮您的呢？' ])
            #cookie没有处理好，没有清除cookie导致20次请求后，请求体发送过大，打开聊天页失败
            self.aidriver.driver.delete_all_cookies()


    def case9(self):
        '''
        性别 - 多问法进入测试性别
        '''
        what_is_my_sexs = []
        what_is_my_sex_1 = [u'我{0}性别{1}'.format(x,y) for x in (u'的',u'',) for y in (u'是什么',u'是啥',) ]
        what_is_my_sex_2 = [u'{0}是{1}{2}'.format(x,y,z) for x in (u'我',u'我的性别',)  for y in (u'男',u'女',)
                             for z  in (u'吗',u'么',)]

        what_is_my_sex_3 = [u'{0}是{1}{2}{3}'.format(x,y,z,k) for x in (u'我',u'我的性别',) for y in (u'男',u'女',)
                        for z in (u'的',u'人',u'生',u'孩',)  for k in (u'吗',u'么',)]

        what_is_my_sex_4 = [u'我{0}男{1}还是女{2}'.format(x,y,z) for x in (u'是',u'',) for y in (u'的',u'人',u'生',u'孩',)
                        for z in (u'的',u'人',u'生',u'孩',)]

        what_is_my_sex_5 = [u'我是男是女{}'.format(x) for x in (u'呢',u'吗',)]
        what_is_my_sex_6 = [u'{0}我{1}性别{2}'.format(x,y,z) for x in (u'请问',u'你知道',) for y in (u'的',u'',)
                             for z in (u'是？',u'是什么',u'吗？',)]

        what_is_my_sex_7 = [u'我{0}性别？'.format(x) for x in (u'的',u'',)]
        what_is_my_sex_8 = [u'{0}性别呢'.format(x) for x in (u'的',u'',)]
        what_is_my_sex_9 = [u'我{0}{1}性别'.format(x,y) for x in (u'是',u'',) for y in (u'什么',u'啥',)]

        what_is_my_sexs = what_is_my_sex_1 + what_is_my_sex_2 + what_is_my_sex_3 + what_is_my_sex_4 + what_is_my_sex_5\
                           + what_is_my_sex_6 + what_is_my_sex_7 + what_is_my_sex_8 + what_is_my_sex_9

        for what_is_my_sex in what_is_my_sexs:
            self.aidriver.open_chat_page()
            self.aidriver.send(what_is_my_sex)
            self.aidriver.checkin([u'我还不知道呢，您能告诉我吗？' ])
            self.aidriver.driver.delete_all_cookies()


    def case10(self):
        '''
        性别 - 多问法回答性别
        '''
        my_sex_is_1 = [u'{is_word}{sex}'.format(is_word = is_words,sex = sexs)
                       for sexs in (u'男',u'女',)
                       for is_words in (u'是',u'',u'我是',u'性别',)
                       ]

        my_sex_is_2 = [u'{is_word}{sex}{people}'.format(is_word = is_words,people = peoples,sex = sexs)
                       for is_words in (u'是', u'', u'我是', u'性别',)
                       for sexs in (u'男',u'女',)
                       for peoples in (u'的',u'人',u'生',u'孩',u'性',)
                       ]

        my_sex_iss = my_sex_is_1 + my_sex_is_2


        for my_sex_is in my_sex_iss:
            self.aidriver.open_chat_page()
            self.aidriver.send(u'我的性别是什么？')
            self.aidriver.send(my_sex_is)
            self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？' ])
            self.aidriver.driver.delete_all_cookies()
            

    def case11(self):
        '''
        年龄 - 多问法进入测试年龄
        '''
        what_is_my_age_1 = [u'{age}{how}'.format(age = ages,how=hows)
                       for ages in (u'年龄',u'年纪',)
                       for hows in (u'呢',u'多少',u'好多',)
                       ]

        what_is_my_age_2 = [u'{question}我{is_word}{age}'.format(age = ages,is_word=is_words,question =questions)
                       for ages in (u'年龄',u'年纪',)
                       for is_words in (u'的',u'',)
                       for questions in (u'请问',u'你知道',)
                       ]

        what_is_my_age_3 = [u'{question}我{age}'.format(age = ages,question =questions)
                       for ages in (u'多大',u'多大年纪',u'几岁',u'多少岁',)
                       for questions in (u'请问',u'你知道',)
                       ]


        what_is_my_ages = what_is_my_age_1 + what_is_my_age_2 + what_is_my_age_3


        for what_is_my_age in what_is_my_ages:
            self.aidriver.open_chat_page()
            self.aidriver.send(what_is_my_age)
            self.aidriver.checkin([u'我还不太清楚您的年龄呢，你能告诉我吗？', u'这个我还不知道呢，要不您直接告诉我吧。'])
            self.aidriver.driver.delete_all_cookies()


    def case12(self):
        '''
        年龄 - 多问法回答年龄
        '''
        ages =(u'13',u'100')
        years_in = (u'1984', u'00', u'九零', u'零零', u'一九八四',)
        my_age_is_1 = [u'{iam}{age}{unit}'.format(age = ages,unit=units,iam = iams)
                       for ages in ages
                       for units in (u'岁', u'',)
                       for iams in (u'我', u'', u'年龄', u'年纪')
                       ]

        my_age_is_2 = [u'{iam}{is_word}{year}年的'.format(year = years,iam=iams,is_word = is_words)
                       for years in years_in
                       for is_words in (u'是', u'为', u'出生于', u'',)
                       for iams in (u'我', u'',)
                       ]
        my_age_is_3 = [u'{iam}{year}出生{accessory}'.format(year = years,iam = iams, accessory=accessorys)
                       for years in years_in
                       for iams in (u'我', u'',)
                       for accessorys in (u'的', u'',)
                       ]
        my_age_iss = my_age_is_1 + my_age_is_2 + my_age_is_3

        for my_age_is in my_age_iss:
            self.aidriver.open_chat_page()
            self.aidriver.send(u'我多大了？')
            self.aidriver.send(my_age_is)
            self.aidriver.checkin_and_log(my_age_is,[u'好的，我清楚了，有什么可以帮您的呢？', ])
            self.aidriver.driver.delete_all_cookies()


    def case13(self):
        '''
        身高 - 多问法进入身高测试
        '''
        what_is_my_height_1 = [u'{}'.format(word)
                       for word in (u'我多高', u'身高呢',)
                       ]
        what_is_my_height_2 = [u'我多少{}'.format(word)
                       for word in (u'米', u'厘米',u'公分',u'尺',u'cm',u'CM',)
                       ]
        what_is_my_height_3 = [u'{iam}身高{word}'.format(iam=iams,word=words)
                       for iams in (u'我',u'',)
                       for words in (u'多少', u'好多',)
                       ]
        what_is_my_height_4 = [u'{question}我{word}身高'.format(question=questions,word=words)
                       for questions in (u'请问',u'你知道',u'',)
                       for words in (u'的', u'',)
                       ]
        what_is_my_heights = what_is_my_height_1 + what_is_my_height_2 + what_is_my_height_3 + what_is_my_height_4
        for what_is_my_height in what_is_my_heights:
            self.aidriver.open_chat_page()
            self.aidriver.send(what_is_my_height)
            self.aidriver.checkin([u'这个可难倒我了，要不您告诉我吧。', ])
            self.aidriver.driver.delete_all_cookies()


    def case14(self):
        '''
        身高 - 多问法回答身高
        '''
        my_height_is_1 = [u'{}1米7'.format(word)
                       for word in (u'我', u'',)
                       ]
        my_height_is_2 = [u'{}{}'.format(word,height)
                       for word in (u'我', u'',)
                       for height in (u'1.7米', u'170厘米',u'510公分',u'5.1尺',u'170cm',u'170CM',)
                       ]

        my_height_iss = my_height_is_1 + my_height_is_2
        for my_height_is in my_height_iss:
            self.aidriver.open_chat_page()
            self.aidriver.send(u'我身高多少?')
            self.aidriver.send(my_height_is)
            self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？', ])
            self.aidriver.driver.delete_all_cookies()

    def case15(self):
        '''
        体重 - 多问法进入体重测试
        '''
        what_is_my_weight_1 = [u'{}'.format(word)
                       for word in (u'体重呢',)
                       ]
        what_is_my_weight_2 = [u'我{}'.format(word)
                       for word in (u'多重', u'多沉',)
                       ]
        what_is_my_weight_3 = [u'{iam}体重{word}'.format(iam=iams,word=words)
                       for iams in (u'我',u'',)
                       for words in (u'多少', u'好多',)
                       ]
        what_is_my_weight_4 = [u'{question}我{word}体重'.format(question=questions,word=words)
                       for questions in (u'请问',u'你知道',u'',)
                       for words in (u'的', u'',)
                       ]
        what_is_my_weight_5 = [u'我多少{word}'.format(word=words)
                       for words in (u'公斤', u'千克', u'kg', u'斤', u'磅',)
                       ]
        what_is_my_weights = what_is_my_weight_1 + what_is_my_weight_2 + what_is_my_weight_3 + \
                             what_is_my_weight_4 + what_is_my_weight_5
        for what_is_my_weight in what_is_my_weights:
            self.aidriver.open_chat_page()
            self.aidriver.send(what_is_my_weight)
            self.aidriver.checkin([u'这个可难倒我了，你可以告诉我您的体重吗？', ])
            self.aidriver.driver.delete_all_cookies()

    def case16(self):
        '''
        体重 - 多问法回答体重
        '''
        my_weight_is_1 = [u'我{}'.format(word)
                       for word in (u'60公斤', u'60千克',u'60kg',u'60KG', u'60kG', u'60Kg', u'132.3磅',)
                       ]
        my_weight_is_2 = [u'{}{}{}{}'.format(x,y,z,k)
                       for x in (u'我',u'',)
                       for y in (u'体重',u'',)
                       for z in (u'是',u'为',u'',)
                       for k in (u'60公斤', u'60千克',u'60kg',u'60KG', u'60kG', u'60Kg', u'132.3磅',)
                       ]
        my_weight_iss = my_weight_is_1 + my_weight_is_2
        for my_weight_is in my_weight_iss:
            self.aidriver.open_chat_page()
            self.aidriver.send(u'我多重?')
            self.aidriver.send(my_weight_is)
            # self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？', ])
            self.aidriver.checkin_and_log(my_weight_is,[u'好的，我清楚了，有什么可以帮您的呢？', ])
            self.aidriver.driver.delete_all_cookies()

    def case17(self):
        '''
        血型 - 多问法进入血型测试
        '''
        what_is_my_bloodtype_1 = [u'{}'.format(word)
                       for word in (u'血型呢',)
                       ]
        what_is_my_bloodtype_2 = [u'血型是{}'.format(word)
                       for word in (u'什么', u'啥',)
                       ]
        what_is_my_bloodtype_3 = [u'我{}{}'.format(x,y)
                       for x  in (u'什么',u'啥',)
                       for y in (u'型', u'型血',u'血型',)
                       ]
        what_is_my_bloodtype_4 = [u'{question}我{word}血型'.format(question=questions,word=words)
                       for questions in (u'请问',u'你知道',u'',)
                       for words in (u'的', u'',)
                       ]

        what_is_my_bloodtypes = what_is_my_bloodtype_1 + what_is_my_bloodtype_2 + what_is_my_bloodtype_3 + \
                             what_is_my_bloodtype_4
        for what_is_my_bloodtype in what_is_my_bloodtypes:
            self.aidriver.open_chat_page()
            self.aidriver.send(what_is_my_bloodtype)
            # self.aidriver.checkin([u'我也想知道您是什么血型哦',u'您还没告诉您是什么血型呢',u'这个我还不知道呢，您能告诉我吗？', ])
            self.aidriver.checkin_and_log(what_is_my_bloodtype,[u'我也想知道您是什么血型哦',u'您还没告诉您是什么血型呢',u'这个我还不知道呢，您能告诉我吗？', ])
            self.aidriver.driver.delete_all_cookies()

    def case18(self):
        '''
        血型 - 多问法回答血型测试
        '''
        my_bloodtype_is_1 = [u'{}{}{}'.format(x,y,z)
                       for x in (u'我',)
                       for y in (u'A',u'B',u'O',u'AB',u'a',u'b',u'ab',u'o',)
                       for z in (u'血型',u'型',u'型血',)
                       ]
        my_bloodtype_iss = my_bloodtype_is_1
        for my_bloodtype_is in my_bloodtype_iss:
            self.aidriver.open_chat_page()
            self.aidriver.send(u'请问我血型?')
            self.aidriver.send(my_bloodtype_is)
            self.aidriver.checkin([u'好的，我清楚了，有什么可以帮您的呢？', ])
            self.aidriver.driver.delete_all_cookies()

















    def case23(self):
        '''
        理财场景不对
        '''
        self.aidriver.send(u'我要理财')
        self.aidriver.send(u'3.00%')
        self.aidriver.send(u'1年')
        self.aidriver.send(u'五万')
        self.aidriver.check(u'2017年同心众盈网银专享保本型第24期\n3%\n年化收益率\n12个月\n理财期限\n点击查看详情')

