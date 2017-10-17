# -*- coding:utf-8 -*-


class A(object):
    def __init__(self, **kwargs):
        self._data = kwargs

    def __getitem__(self, key):
        return self._data.get(key)

    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        self._data.pop(key, None)

    def __contains__(self, key):
        return key in self._data.keys()

a = A(x=1, y=2)

print a["x"]  # 1

a["z"] = 3
print "z" in a  # True

del a["y"]

print a._data  # {'x': 1, 'z': 3}
