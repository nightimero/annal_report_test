# -*- coding: utf-8 -*-

#多线程实现itchat发送消息

import threadpool
import itchat

def smm(msglist):
    # global itchat
    itchat.send_msg(msglist,name[0])







if '__name__' == "__mian__":
    msg_list=[u'test1',u'test2',u'test3',u'test4',u'test5']
    itchat.auto_login()
    PROCESS = 2
    pool = threadpool.ThreadPool(PROCESS)
    requests = threadpool.makeRequests(smm,msg_list)
    [pool.putRequest(req) for req in requests]
    pool.wait()
