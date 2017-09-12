# -*- coding:utf-8 -*-
from selenium import webdriver
import random
import time

ip = "119.23.232.160:8888"
uid = random.randint(1,99999999)
yes_word = [u'没问题',u'行啊',u'行吧',u'行的',u'可以',u'好啊',u'好的',u'好吧',u'接受',u'愿意',u'行',u'好',u'是',u'恩',u'嗯',]
not_word = [u'不太接受',u'不太愿意',u'不太想',u'不接受',u'不愿意',u'不需要',u'千万别',u'办不到',u'做不到',u'不得行',u'不行',u'不想',u'不是',u'不用',u'不要',u'不愿',u'没有',u'不会',u'不能',u'不了',u'不必',u'无需',u'无须',u'切勿',u'不會',u'不可',u'不肯',u'勿需',u'切莫',u'勿要',u'无法',u'無法',u'不好',u'不',u'没',u'无',u'否',u'非',u'勿',u'弗',u'莫',u'毋',u'未',u'别',u'無',u'休',]
unknown_answer = [u'在投资理财上我可是专家，可是您这问题我还需要继续学习哟~',
                  u'AiKNOWN夜观天象，您这个话我没法儿接~还是问问我理财投资的问题吧',
                  u'这个问题AiKNOWN还在学习中哦，问问我投资理财的问题吧，我可是专业的哦~']



driver = webdriver.Chrome()
driver.get("http://"+ip+"/html/chat.html?uid="+str(uid))

def case1():
    '''
    联络员如何登陆年报
    是
    是
    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(yes_word))
    check(u'是否\n或者输入您期望的结果')
    check2(u'建议您办理证书登录年报最为方便，你是否接受？')
    send(random.choice(yes_word))
    check(u'请根据以下步骤操作证书新领：1.打开http://online.icinfo.cn/eppnet/sys/enPackageBuyAction.do?'
          u'_id=150466821484,点击"证书新领"-"法人单位证书"根据页面提示操作至支付完成。'
          u'（温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书）')

def case2():
    '''
    联络员如何登陆年报
    是
    否
    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(yes_word))
    check(u'是否\n或者输入您期望的结果')
    check2(u'建议您办理证书登录年报最为方便，你是否接受？')
    send(random.choice(not_word))
    check(u'根据以下步骤联络员登录年报：请打开http://118.178.33.191/reg/client/login/all,'
          u'点击"工商联络员登录"输入带星号信息，输入获取到验证码点击“登录”即可。')

def case3():
    '''
    联络员如何登陆年报
    否
    启运智创有限公司
    握奇
    是
    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(not_word))
    check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
    send(random.choice([u'启运智创有限公司', ]))
    check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
    check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
    send(random.choice([u'握奇', ]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'您手上证书是旧版证书，使用起来不太稳定，建议您重新补办新版证书。是否补办新版证书？')
    send(random.choice(yes_word))
    check(u'请根据以下步骤操作证书补办：打开'
          u'http://online.icinfo.cn/eppnet/'
          u'选择证书补办“立即办理”根据页面提示操作至支付完成。（'
          u'温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书。）')

def case4():
    '''
    联络员如何登陆年报
    否
    启运智创有限公司
    握奇
    否
    是win7 64以上
    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(not_word))
    check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
    send(random.choice([u'启运智创有限公司', ]))
    check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
    check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
    send(random.choice([u'握奇', ]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'您手上证书是旧版证书，使用起来不太稳定，建议您重新补办新版证书。是否补办新版证书？')
    send(random.choice(not_word))
    check(u'win64以上系统xp/win32位系统\n或者输入您期望的结果')
    check2(u'请右键点击桌面上“我的电脑”/“计算机”-属性，查看电脑属性。请问你系统是64位以上还是32位？')
    send(random.choice([u'win64以上系统',]))
    check(u'请根据以下步骤操作证书补办：打开'
          u'http://online.icinfo.cn/eppnet/选择证书补办“立即办理”根据页面提示操作至支付完成。'
          u'（温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书。）')

def case5():
    '''
    联络员如何登陆年报
    否
    启运智创有限公司
    握奇
    否
    是xp、win732
    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(not_word))
    check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
    send(random.choice([u'启运智创有限公司', ]))
    check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
    check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
    send(random.choice([u'握奇', ]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'您手上证书是旧版证书，使用起来不太稳定，建议您重新补办新版证书。是否补办新版证书？')
    send(random.choice(not_word))
    check(u'win64以上系统xp/win32位系统\n或者输入您期望的结果')
    check2(u'请右键点击桌面上“我的电脑”/“计算机”-属性，查看电脑属性。请问你系统是64位以上还是32位？')
    send(random.choice([u'xp/win32位系统',]))
    check(u'打开“联连客户端”账号登录之后，选择“工商网上年报”点击“数字证书登录”根据提示操作即可。')

def case6():
    '''
    联络员如何登陆年报
    否
    启运智创有限公司
    没有证书
    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(not_word))
    check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
    send(random.choice([u'启运智创有限公司', ]))
    check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
    check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
    send(random.choice([u'没有证书', ]))
    check(u'请根据以下步骤操作证书补办：打开http://online.icinfo.cn/eppnet/'
          u'选择证书补办“立即办理”根据页面提示操作至支付完成。'
          u'（温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书。）')

def case7():
    '''
    联络员如何登陆年报
    否
    启运智创有限公司
    飞天、海泰、龙脉
    是
    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(not_word))
    check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
    send(random.choice([u'启运智创有限公司', ]))
    check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
    check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
    send(random.choice([u'飞天',u'海泰',u'龙脉', ]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'请插上证书，桌面上是否有联连客户端3.0图标，如图：')
    send(random.choice(yes_word))
    check(u'打开“联连客户端”账号登录之后，选择“工商网上年报”点击“数字证书登录”根据提示操作即可。')

def case8():
    '''
    联络员如何登陆年报
    否
    启运智创有限公司
    飞天、海泰、龙脉
    否
    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(not_word))
    check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
    send(random.choice([u'启运智创有限公司', ]))
    check(u'握奇飞天海泰龙脉\n或者输入您期望的结果')
    check2(u'您公司查询到之前领过证书，根据今年年报要求，只能证书登录，证书图片如下：\n握奇证书:\n飞天证书:\n海泰证书:\n龙脉证书:')
    send(random.choice([u'飞天',u'海泰',u'龙脉', ]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'请插上证书，桌面上是否有联连客户端3.0图标，如图：')
    send(random.choice(not_word))
    check(u'打开http://www.icinfo.cn/html/download.action，点击“联连客户端”下载，根据提示安装即可')

def case9():
    '''
    联络员如何登陆年报
    否
    其他有限公司
    是
    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(not_word))
    check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
    send(random.choice([u'其他有限公司', ]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'您公司成立的时间是否2015年12月31日之后')
    send(random.choice(yes_word))
    check(u'请根据以下步骤操作证书新领：'
          u'1.打开http://online.icinfo.cn/eppnet/sys/enPackageBuyAction.do?_id=150466821484,'
          u'点击"证书新领"-"法人单位证书"根据页面提示操作至支付完成。'
          u'（温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书）')

def case10():
    '''
    联络员如何登陆年报
    否
    其他有限公司
    否
    是
    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(not_word))
    check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
    send(random.choice([u'其他有限公司', ]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'您公司成立的时间是否2015年12月31日之后')
    send(random.choice(not_word))
    check(u'是否\n或者输入您期望的结果')
    check2(u'建议您办理证书登录年报最为方便，你是否接受？')
    send(random.choice(yes_word))
    check(u'请根据以下步骤操作证书新领：1.打开'
          u'http://online.icinfo.cn/eppnet/sys/enPackageBuyAction.do?_id=150466821484,'
          u'点击"证书新领"-"法人单位证书"根据页面提示操作至支付完成。'
          u'（温馨提示：费用支付之后需邮寄资料进行审核，审核通过3-5个工作日会寄出证书）')

def case11():
    '''
    联络员如何登陆年报
    否
    其他有限公司
    否
    否
    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(not_word))
    check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
    send(random.choice([u'其他有限公司', ]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'您公司成立的时间是否2015年12月31日之后')
    send(random.choice(not_word))
    check(u'是否\n或者输入您期望的结果')
    check2(u'建议您办理证书登录年报最为方便，你是否接受？')
    send(random.choice(not_word))
    check(u'根据以下步骤联络员登录年报：请打开'
          u'http://118.178.33.191/reg/client/login/all,'
          u'点击"工商联络员登录"输入带星号信息，输入获取到验证码点击“登录”即可。')

def case12():
    '''
    切换场景用例

    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice(not_word))
    check(u'请告知公司名称，帮你查询（后台判断是否可以关联查询有无领过证书）')
    send(random.choice([u'其他有限公司', ]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'您公司成立的时间是否2015年12月31日之后')
    send(random.choice(not_word))
    check(u'是否\n或者输入您期望的结果')
    check2(u'建议您办理证书登录年报最为方便，你是否接受？')
    send(random.choice(not_word))
    check(u'根据以下步骤联络员登录年报：请打开'
          u'http://118.178.33.191/reg/client/login/all,'
          u'点击"工商联络员登录"输入带星号信息，输入获取到验证码点击“登录”即可。')
    send(random.choice([u'今天天气怎样',u'我要买冰箱', ]))
    checkin(unknown_answer)

def case13():
    '''
    切换场景用例

    :return:
    '''
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')
    send(random.choice([u'我要投资',u'我要理财', ]))
    check(u'推荐表单\n收益率\n理财期\n起购金额')

def case14():
    '''
    切换场景用例

    :return:
    '''
    send(random.choice([u'我要投资', u'我要理财', ]))
    send(random.choice([u'联络员如何登陆年报',]))
    check(u'是否\n或者输入您期望的结果')
    check2(u'你公司是否属于宁波地区企业/个体户？')

def case15():
    case13()
    case14()

if __name__ == '__main__':
    def main():
        for i in range(1,14):
            print '开始第{}个测试用例'.format(i)
            globals()['case'+str(i)]()
    def test():
        list =range(1,14)
        #indices = [3,4,5,9]  #第一次测试未通过用例
        # indices = [7,8]       #第二次测试未通过用例
        indices = [1]          #第三次测试未通过用例
        leave_list = [ i for j,i in enumerate(list) if j+1 not in indices]
        for i in leave_list:
            print '\n\n\n\n===开始第{}个测试用例==='.format(i)
            globals()['case'+str(i)]()
    for i in range(100):
        print u'*********开始第{}个循环************'.format(i+1)
        main()
        # test()aichat.py