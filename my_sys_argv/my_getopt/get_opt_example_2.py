# -*- coding: utf-8 -*-
import sys
import getopt


def my_getopt():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'd:f:h', ['days=', 'files=', 'help'])
    except getopt.GetoptError:
        usage()
        sys.exit()

    print (opts)
    print (args)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--days"):
            day = a
        elif o in ("-f", "--files"):
            files = a
    print (day)
    print (files)


def usage():
    pass

# todo: use it

if __name__ == '__main__':
    my_getopt()