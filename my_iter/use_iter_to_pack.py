# -*- coding:utf-8 -*-

# 有一个偶数项的列表 a = ["foo", 2, "bar", 4, "far", 6]，希望对每两个相邻的两个元素打包，是为一组, 
# 使得结果如下是这样的 [("foo", 2), ("bar", 4), ("far", 6)]。如果是要打包是每三个一组呢？
# 
# 有很多方法可以解决，下面使用迭代器进行处理，大概代码如下：

b = [iter([1, 2, 3, 4, 5])]
print b
print b * 2
print b[0]
print id(b)

a = ["foo", 2, "bar", 4, "far", 6]
c = iter(a)
# 这里的zip中的* 不是指针，是不确定参数个数，按照列表，传入多少个参数就是多少个。
# func(*args)的意思。
print zip(*([iter(a)]*2))  # [('foo', 2), ('bar', 4), ('far', 6)]
print zip(*([c]*2))        # [('foo', 2), ('bar', 4), ('far', 6)]
print zip(*([c]*2))  # 这里果然返回的是空，看来真的是利用的next不能回头的特性。
print [a]*2

group_adjacent = lambda x, k: zip(*([iter(x)] * k))
# 虽然这样写不规范，不符合PEP规范，但是呢。在命令行里用这个倒是挺方便的。一行搞定。
# 一行式的优美。
# [] + iter 是什么意思呢？利用到了迭代器next之后不回头的特性。
# group_adjacent = lambda x, k: zip(*(iter(x) * k))  # 这样缺少中括号是不行的。

print group_adjacent(a, 2)  # [('foo', 2), ('bar', 4), ('far', 6)]
print group_adjacent(a, 3)
print 'four pack:', group_adjacent(a, 4)  # 只返回这样的。four pack: [('foo', 2, 'bar', 4)]，丢失了两个元素。
print 'test pack with none:', zip([1, 2, 3, 4], [1, 2, None, None])  # [(1, 1), (2, 2), (3, None), (4, None)]
# 这里证明了，iterator是惰性计算。zip是一个元素一个元素返回的。然后异常以后，第二个元素没有返回。
# zip和for一样，内部处理了StopIteration的异常，而没有抛出。


def group_it(x, k):
    return zip(*([x]*k))

print group_it(a, 2)
print group_it(a, 3)
print group_it(iter(a), 2)

print zip([1, 2], [3, 4])
