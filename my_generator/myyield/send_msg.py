def gen():
    while True:
        hello_world = yield
        print(hello_world)

g = gen()


# 在调用send方法前，必须先调用一次__next__，让生成器执行到 yield 语句处，
#  才能进行赋值。外面加上 while 循环是为了避免出现send之后， .
# 生成器没有 yield 语句了，抛出 StopIteration 的情况。
next(g)  # 原来next也可以作为一个函数使用。


g.send("WTF!")
g.send("what the fuck!!")
g.next()
g.next()

# todo：http://dhcmrlchtdj.github.io/sia/post/2012-11-20/python_yield.html
# todo：https://liam0205.me/2017/06/30/understanding-yield-in-python/
# todo：http://www.oschina.net/translate/improve-your-python-yield-and-generators-explained
# todo：https://foofish.net/understanding-yield.html
