# -*- coding: utf-8 -*-
import json

# 1.use cls
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


print json.dumps(2 + 1j, cls=ComplexEncoder)
# '[2.0, 1.0]'
print ComplexEncoder().encode(2 + 1j)
# '[2.0, 1.0]'
print list(ComplexEncoder().iterencode(2 + 1j))
# ['[', '2.0', ', ', '1.0', ']']

# 2.use sort_key
print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
# {"a": 0, "b": 0, "c": 0}
