# -*- coding: utf-8 -*-
import json

# 1. use object_pairs_hook
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict

data = json.loads(s, object_pairs_hook=OrderedDict)  # 参数： object_pairs_hook
print data
# OrderedDict([(u'name', u'ACME'), (u'shares', 50), (u'price', 490.1)])


# 2. use object_hook , here use func: as_complex
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


print json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex)
# (1 + 2j)

# 3.use decimal
import decimal

print json.loads('1.1', parse_float=decimal.Decimal)
print type(json.loads('1.1', parse_float=decimal.Decimal))
# Decimal('1.1')

print json.loads('1.1')
print type(json.loads('1.1'))
# Decimal('1.1')
