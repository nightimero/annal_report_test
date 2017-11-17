# -*- coding: utf-8 -*-
# An example using only Unix style options:
#
# >>> import getopt
# >>> args = '-a -b -cfoo -d bar a1 a2'.split()
# >>> args
# ['-a', '-b', '-cfoo', '-d', 'bar', 'a1', 'a2']
# >>> optlist, args = getopt.getopt(args, 'abc:d:')
# >>> optlist
# [('-a', ''), ('-b', ''), ('-c', 'foo'), ('-d', 'bar')]
# >>> args
# ['a1', 'a2']
# Using long option names is equally easy:
#
# >>> s = '--condition=foo --testing --output-file abc.def -x a1 a2'
# >>> args = s.split()
# >>> args
# ['--condition=foo', '--testing', '--output-file', 'abc.def', '-x', 'a1', 'a2']
# >>> optlist, args = getopt.getopt(args, 'x', [
# ...     'condition=', 'output-file=', 'testing'])
# >>> optlist
# [('--condition', 'foo'), ('--testing', ''), ('--output-file', 'abc.def'), ('-x', '')]
# >>> args
# ['a1', 'a2']
