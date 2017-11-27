# -*- coding:utf-8 -*-
# todo: https://docs.python.org/2/library/collections.html
# todo: http://www.cnblogs.com/herbert/p/3468294.html
from collections import OrderedDict


class Point(tuple):
    """Point(x, y)"""

    __slots__ = ()

    _fields = ('x', 'y')

    def __new__(_cls, x, y):
        """Create new instance of Point(x, y)"""
        return tuple.__new__(_cls, (x, y))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        """Make a new Point object from a sequence or iterable"""
        result = new(cls, iterable)
        if len(result) != 2:
            raise TypeError('Expected 2 arguments, got %d' % len(result))
        return result

    def __repr__(self):
        """Return a nicely formatted representation string"""
        return 'Point(x=%r, y=%r)' % self

    def _asdict(self):
        """Return a new OrderedDict which maps field names to their values"""
        return OrderedDict(zip(self._fields, self))

    def _replace(self, **kwds):
        """Return a new Point object replacing specified fields with new values"""
        result = self._make(map(kwds.pop, ('x', 'y'), self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % kwds.keys())
        return result

    def __getnewargs__(self):
        """Return self as a plain tuple.  Used by copy and pickle."""
        return tuple(self)

    __dict__ = property(_asdict)

    def __getstate__(self):
        """Exclude the OrderedDict from pickling"""
        pass

    x = property(_itemgetter(0), doc='Alias for field number 0')

    y = property(_itemgetter(1), doc='Alias for field number 1')