# -*- coding:utf-8 -*-
import threading, multiprocessing
# 确实在linux上可以跑满。在windows上影响不大。只有一个核心在工作。这是纯计算的任务。所以可以跑满。
# 在虚拟机上 双核可以跑满。 四核不能跑满，应该是受到了虚拟机的限制。和GIL锁影响
# 四核的时候，主机的cpu已经80%以上了。虚拟机才160%

# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
# 任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，
# 让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
# 所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

# 这样执行也不是原子性的，也不能保证线程安全。主要是为了保证解释器执行。

# Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。


def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

# todo: 使用pypy运行python程序 pypy 没有gil锁？
# 看了上面的评论，我很难理解为何我的python程序可以吧12个核都跑满，不管用python2.6 还是2.7 还是pypy。
# 真不知道python程序只能跑在一个核上的谣言是被这些半吊子传成这样很凶残的状况。
# 一个半吊子python程序员写的程序非常可能在性能上高于一个半吊子c程序员的程序。
# gil是针对一个python解释器进程而言的，这才是真相，如果解释器可以多进程解释执行，那就不存在gil的问题了，
# 同样，他也不会导致你多个解释器跑在同一个核上。

# GIL是什么
#
# 首先需要明确的一点是GIL并不是Python的特性，它是在实现Python解析器(CPython)时所引入的一个概念。
# 就好比C++是一套语言（语法）标准，但是可以用不同的编译器来编译成可执行代码。
# 有名的编译器例如GCC，INTEL C++，Visual C++等。Python也一样，同样一段代码可以通过CPython，
# PyPy，Psyco等不同的Python执行环境来执行。像其中的JPython就没有GIL。然而因为CPython是大部分环境下默认的Python执行环境。
# 所以在很多人的概念里CPython就是Python，也就想当然的把GIL归结为Python语言的缺陷。
# 所以这里要先明确一点：GIL并不是Python的特性，Python完全可以不依赖于GIL
# 参考http://cenalulu.github.io/python/gil-in-python/  写的真好。
