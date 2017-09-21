# -*- coding: utf-8 -*-
import threadpool
import time


def now_time(n):
  print 'Starting at %s' % time.ctime()
  time.sleep(n)
  return 'Ending at %s' % time.ctime()


def print_now(request, n):
    # pass
  print '%s - %s' % (request.requestID, n)  #这里的requestID只是显示下，没实际意义

pool = threadpool.ThreadPool(5)
reqs = threadpool.makeRequests(now_time, range(1, 11), print_now)
[pool.putRequest(req) for req in reqs]
pool.wait()