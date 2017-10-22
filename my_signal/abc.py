# -*- coding:utf-8 -*-
import signal
import time
__author__ = 'shawn'
term = False


def sighandler(signum, frame):
    print "terminate signal received..."
    global term
    term = True


def set_signal():
    signal.signal(signal.SIGTERM, sighandler)
    signal.signal(signal.SIGINT, sighandler)


def clear_signal():
    signal.signal(signal.SIGTERM, 0)
    signal.signal(signal.SIGINT, 0)


set_signal()
while not term:
    print "hello"
    time.sleep(1)

print "jumped out of while loop"

# todo: how to trigger the next
clear_signal()
term = False
for i in range(5):
    if term:
        break
    else:
        print "hello, again"
        time.sleep(1)
