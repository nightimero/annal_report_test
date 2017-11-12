# -*- coding:utf-8 -*-
import collections
import threading
import time

candle = collections.deque(xrange(100))

def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print '%s-->%8s: %s' % (threading.current_thread().name, direction, next)
            time.sleep(0.1)
    print '%8s done' % direction
    return

left1 = threading.Thread(target=burn, name='thread-left1', args=('Left', candle.popleft))
left2 = threading.Thread(target=burn, name='thread-left2', args=('Left', candle.popleft))
right1 = threading.Thread(target=burn, name='thread-right1', args=('Right', candle.pop))
right2 = threading.Thread(target=burn, name='thread-right2', args=('Right', candle.pop))

left1.start()
left2.start()
right1.start()
right2.start()

left1.join()
left2.join()
right1.join()
right2.join()
