# -*- coding: utf-8 -*-
# 使用optionparser模块来解析
#
# optionparser的执行过程：
#
# 导入optionparser ： from optparse import OptionParser
# 构造optionparser的对象：parser = OptionParser()
# 往optionparser对象中增加option ：parser.add_option()
#
# 调用optionparser的解析函数：(options, args) = parser.parse_args()
# 在options中使用解析到的options，在args中使用其他的args。


def my_optionparser():
    from optparse import OptionParser
    parser = OptionParser(usage="locust [options] [LocustClass [LocustClass2 ... ]]", version="1.0.1",)
    # 不能使用test
    # parser = OptionParser(usage="locust [options] [LocustClass [LocustClass2 ... ]]", version="1.0.1", test='ddd')
    parser.add_option("-f", "--file", dest="filename",
                      help="write report to FILE", metavar="FILE")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="don't print status messages to stdout")
    (options, args) = parser.parse_args()
    print (options.filename)
    print (options.verbose)
    print (args)


if __name__ == '__main__':
    my_optionparser()
