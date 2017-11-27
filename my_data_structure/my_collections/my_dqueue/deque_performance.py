# -*- coding:utf-8 -*-
import time
import Queue
import collections

q = collections.deque()
t0 = time.clock()
for i in xrange(1000000):
    q.append(1)
for i in xrange(1000000):
    q.popleft()
print 'deque', time.clock() - t0

q = Queue.Queue(2000000)
t0 = time.clock()
for i in xrange(1000000):
    q.put(1)
for i in xrange(1000000):
    q.get()
print 'Queue', time.clock() - t0

q = []
t0 = time.clock()
for i in xrange(100000):
    q.append(i)

for i in xrange(100000):  # insert 才是罪魁祸首
    q.insert(0, i)

print 'list ', time.clock() - t0
