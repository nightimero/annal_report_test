# -*- coding: utf-8 -*-
# !/usr/bin/python

import sys, getopt


def main(argv):
    inputfile = ''
    outputfile = ''
    verbose = False
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile=", "verbose"])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile> please'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("--verbose"):
            verbose = True
    print u'输入的文件为：', inputfile
    print u'输出的文件为：', outputfile
    print u'verbose：', verbose
    print u'没有利用上的参数：', args


if __name__ == "__main__":
    main(sys.argv[1:])


# python my_getopt.py --verbose --ifile fasdf nouse  必须要这样用
# 输入的文件为： fasdf
# 输出的文件为：
# verbose： True
# 没有利用上的参数： ['nouse']
#
# python my_getopt.py --ifile fasdf nouse --verbose

# 输入的文件为： fasdf
# 输出的文件为：
# verbose： False
# 没有利用上的参数： ['nouse', '--verbose']
