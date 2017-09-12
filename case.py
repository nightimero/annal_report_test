# -*- coding:utf-8 -*-
from config import *
import random

class Cases(object):
    def __init__(self,aidriver):
        self.aidriver = aidriver

    def case1(self):
        '''
        联络员如何登陆年报
        是
        是
        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(yes_word))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'建议您办理证书登录年报最为方便，你是否接受？')
        self.aidriver.send(random.choice(yes_word))
        self.aidriver.check(u'请根据以下步骤操作证书新领：1.打开http://online.icinfo.cn/eppnet/sys/enPackageBuyAction.do?'
              u'_id=150466821484,点击"证书新领"-"法人单位证书"根据页面提示操作至支付完成。'
              u'（温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书）')

    def case2(self):
        '''
        联络员如何登陆年报
        是
        否
        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(yes_word))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'建议您办理证书登录年报最为方便，你是否接受？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'根据以下步骤联络员登录年报：请打开http://118.178.33.191/reg/client/login/all,'
              u'点击"工商联络员登录"输入带星号信息，输入获取到验证码点击“登录”即可。')

    def case3(self):
        '''
        联络员如何登陆年报
        否
        启运智创有限公司
        握奇
        是
        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
        self.aidriver.send(random.choice([u'启运智创有限公司', ]))
        self.aidriver.check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
        self.aidriver.check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
        self.aidriver.send(random.choice([u'握奇', ]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'您手上证书是旧版证书，使用起来不太稳定，建议您重新补办新版证书。是否补办新版证书？')
        self.aidriver.send(random.choice(yes_word))
        self.aidriver.check(u'请根据以下步骤操作证书补办：打开'
              u'http://online.icinfo.cn/eppnet/'
              u'选择证书补办“立即办理”根据页面提示操作至支付完成。（'
              u'温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书。）')

    def case4(self):
        '''
        联络员如何登陆年报
        否
        启运智创有限公司
        握奇
        否
        是win7 64以上
        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
        self.aidriver.send(random.choice([u'启运智创有限公司', ]))
        self.aidriver.check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
        self.aidriver.check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
        self.aidriver.send(random.choice([u'握奇', ]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'您手上证书是旧版证书，使用起来不太稳定，建议您重新补办新版证书。是否补办新版证书？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'win64以上xp/win32位\n或者输入您期望的结果')
        self.aidriver.check2(u'请右键点击桌面上“我的电脑”/“计算机”-属性，查看电脑属性。请问你系统是64位以上还是32位？')
        self.aidriver.send(random.choice([u'win64以上系统',]))
        self.aidriver.check(u'请根据以下步骤操作证书补办：打开'
              u'http://online.icinfo.cn/eppnet/选择证书补办“立即办理”根据页面提示操作至支付完成。'
              u'（温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书。）')

    def case5(self):
        '''
        联络员如何登陆年报
        否
        启运智创有限公司
        握奇
        否
        是xp、win732
        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
        self.aidriver.send(random.choice([u'启运智创有限公司', ]))
        self.aidriver.check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
        self.aidriver.check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
        self.aidriver.send(random.choice([u'握奇', ]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'您手上证书是旧版证书，使用起来不太稳定，建议您重新补办新版证书。是否补办新版证书？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'win64以上xp/win32位\n或者输入您期望的结果')
        self.aidriver.check2(u'请右键点击桌面上“我的电脑”/“计算机”-属性，查看电脑属性。请问你系统是64位以上还是32位？')
        self.aidriver.send(random.choice([u'xp/win32位系统',]))
        self.aidriver.check(u'打开“联连客户端”账号登录之后，选择“工商网上年报”点击“数字证书登录”根据提示操作即可。')

    def case6(self):
        '''
        联络员如何登陆年报
        否
        启运智创有限公司
        没有证书
        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
        self.aidriver.send(random.choice([u'启运智创有限公司', ]))
        self.aidriver.check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
        self.aidriver.check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
        self.aidriver.send(random.choice([u'没有证书', ]))
        self.aidriver.check(u'请根据以下步骤操作证书补办：打开http://online.icinfo.cn/eppnet/'
              u'选择证书补办“立即办理”根据页面提示操作至支付完成。'
              u'（温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书。）')

    def case7(self):
        '''
        联络员如何登陆年报
        否
        启运智创有限公司
        飞天、海泰、龙脉
        是
        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
        self.aidriver.send(random.choice([u'启运智创有限公司', ]))
        self.aidriver.check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
        self.aidriver.check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
        self.aidriver.send(random.choice([u'飞天',u'海泰',u'龙脉', ]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'请插上证书，桌面上是否有联连客户端3.0图标，如图：')
        self.aidriver.send(random.choice(yes_word))
        self.aidriver.check(u'打开“联连客户端”账号登录之后，选择“工商网上年报”点击“数字证书登录”根据提示操作即可。')

    def case8(self):
        '''
        联络员如何登陆年报
        否
        启运智创有限公司
        飞天、海泰、龙脉
        否
        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
        self.aidriver.send(random.choice([u'启运智创有限公司', ]))
        self.aidriver.check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
        self.aidriver.check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
        self.aidriver.send(random.choice([u'飞天',u'海泰',u'龙脉', ]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'请插上证书，桌面上是否有联连客户端3.0图标，如图：')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'打开http://www.icinfo.cn/html/download.action，点击“联连客户端”下载，根据提示安装即可')

    def case9(self):
        '''
        联络员如何登陆年报
        否
        其他有限公司
        是
        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
        self.aidriver.send(random.choice([u'其他有限公司', ]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'您公司成立的时间是否2015年12月31日之后')
        self.aidriver.send(random.choice(yes_word))
        self.aidriver.check(u'请根据以下步骤操作证书新领：'
              u'1.打开http://online.icinfo.cn/eppnet/sys/enPackageBuyAction.do?_id=150466821484,'
              u'点击"证书新领"-"法人单位证书"根据页面提示操作至支付完成。'
              u'（温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书）')

    def case10(self):
        '''
        联络员如何登陆年报
        否
        其他有限公司
        否
        是
        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
        self.aidriver.send(random.choice([u'其他有限公司', ]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'您公司成立的时间是否2015年12月31日之后')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'建议您办理证书登录年报最为方便，你是否接受？')
        self.aidriver.send(random.choice(yes_word))
        self.aidriver.check(u'请根据以下步骤操作证书新领：1.打开'
              u'http://online.icinfo.cn/eppnet/sys/enPackageBuyAction.do?_id=150466821484,'
              u'点击"证书新领"-"法人单位证书"根据页面提示操作至支付完成。'
              u'（温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书）')

    def case11(self):
        '''
        联络员如何登陆年报
        否
        其他有限公司
        否
        否
        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
        self.aidriver.send(random.choice([u'其他有限公司', ]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'您公司成立的时间是否2015年12月31日之后')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'建议您办理证书登录年报最为方便，你是否接受？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'根据以下步骤联络员登录年报：请打开'
              u'http://118.178.33.191/reg/client/login/all,'
              u'点击"工商联络员登录"输入带星号信息，输入获取到验证码点击“登录”即可。')

    def case12(self):
        '''
        切换场景用例

        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
        self.aidriver.send(random.choice([u'其他有限公司', ]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'您公司成立的时间是否2015年12月31日之后')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'建议您办理证书登录年报最为方便，你是否接受？')
        self.aidriver.send(random.choice(not_word))
        self.aidriver.check(u'根据以下步骤联络员登录年报：请打开'
              u'http://118.178.33.191/reg/client/login/all,'
              u'点击"工商联络员登录"输入带星号信息，输入获取到验证码点击“登录”即可。')
        self.aidriver.send(random.choice([u'今天天气怎样',u'我要买冰箱', ]))
        self.aidriver.checkin(unknown_answer)

    def case13(self):
        '''
        切换场景用例

        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')
        self.aidriver.send(random.choice([u'我要投资',u'我要理财', ]))
        self.aidriver.check(u'推荐表单\n收益率\n理财期\n起购金额')

    def case14(self):
        '''
        切换场景用例

        :return:
        '''
        self.aidriver.send(random.choice([u'我要投资', u'我要理财', ]))
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'是否\n或者输入您期望的结果')
        self.aidriver.check2(u'你公司是否属于宁波地区企业/个体户？')

    def case15(self):
        '''
        切换场景用例

        :return:
        '''
        self.aidriver.send(random.choice([u'联络员如何登陆年报',]))
        self.aidriver.check(u'请您肯定或否定回答')
        self.aidriver.send(random.choice([u'我要投资',u'我要理财', ]))
        self.aidriver.check(u'推荐表单\n收益率\n理财期\n起购金额')
