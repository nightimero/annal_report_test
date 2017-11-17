# -*- coding: utf-8 -*-
# !/usr/bin/python

import sys, getopt


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
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
    print u'输入的文件为：', inputfile
    print u'输出的文件为：', outputfile
    print u'没有利用上的参数：', args


if __name__ == "__main__":
    main(sys.argv[1:])
