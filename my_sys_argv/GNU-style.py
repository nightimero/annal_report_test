# -*- coding: utf-8 -*-
# GNU-style Option Parsing
#
# New in Python 2.3, an additional function gnu_getopt() was added. It allows option and non-option arguments
#  to be mixed on the command line in any order.

import getopt
import sys

version = '1.0'
verbose = False
output_filename = 'default.out'

print 'ARGV      :', sys.argv[1:]

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'o:v', ['output=',
                                                             'verbose',
                                                             'version=',
                                                             ])
print 'OPTIONS   :', options

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = arg

print 'VERSION   :', version
print 'VERBOSE   :', verbose
print 'OUTPUT    :', output_filename
print 'REMAINING :', remainder
# After changing the call in the previous example, the difference becomes clear:
#
# $ python getopt_gnu.py -v not_an_option --output foo
#
# ARGV      : ['-v', 'not_an_option', '--output', 'foo']
# OPTIONS   : [('-v', ''), ('--output', 'foo')]
# VERSION   : 1.0
# VERBOSE   : True
# OUTPUT    : foo
# REMAINING : ['not_an_option']
# Special Case: --
#
# If getopt encounters -- in the input arguments, it stops processing the remaining arguments as options.
#
# $ python getopt_example.py -v -- --output foo
#
# ARGV      : ['-v', '--', '--output', 'foo']
# OPTIONS   : [('-v', '')]
# VERSION   : 1.0
# VERBOSE   : True
# OUTPUT    : default.out
# REMAINING : ['--output', 'foo']
