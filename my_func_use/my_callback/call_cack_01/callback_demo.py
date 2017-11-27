# -*- coding:utf-8 -*-
from even import *


# 中间函数
# 接受一个生成偶数的函数作为参数
# 返回一个奇数
def getOddNumber(k, getEvenNumber):
    return 1 + getEvenNumber(k)


# 起始函数，这里是程序的主函数
def main():
    k = 1
    # 当需要生成一个2k+1形式的奇数时
    i = getOddNumber(k, double)
    print(i)
    # 当需要一个4k+1形式的奇数时
    i = getOddNumber(k, quadruple)
    print(i)
    # 当需要一个8k+1形式的奇数时
    i = getOddNumber(k, lambda x: x * 8)
    print(i)


if __name__ == "__main__":
    main()

# 作者：no.body
# 链接：https: // www.zhihu.com / question / 19801131 / answer / 27459821
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。