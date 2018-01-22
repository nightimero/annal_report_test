# -*- coding: utf-8 -*-
import json

obj = [[1, 2, 3], 123, 123.123, 'abc', {'key1': (1, 2, 3), 'key2': (4, 5, 6)}]
encodedjson = json.dumps(obj)
print 'the original list:\n', obj
print 'length of obj is:', len(repr(obj))
print 'repr(obj),replace whiteblank with *:\n', repr(obj).replace(' ', '*')
print 'json encoded,replace whiteblank with *:\n', encodedjson.replace(' ', '*')

all_factors_request = {'id_number': 748626784, 'gender': u'\u7537', 'age': 31, 'answers': [{'question_id': '1', 'option_id': '1', 'body_place_id': '2', 'option_content': u'\u75bc\u75db'}, {'question_id': '1', 'option_id': '1', 'body_place_id': '11', 'option_content': u'\u75bc\u75db'}, {'question_id': '1', 'option_id': '1', 'body_place_id': '13', 'option_content': u'\u75bc\u75db'}, {'question_id': '1', 'option_id': '1', 'body_place_id': '14', 'option_content': u'\u75bc\u75db'}, {'question_id': '1', 'option_id': '1', 'body_place_id': '15', 'option_content': u'\u75bc\u75db'}, {'question_id': '1', 'option_id': '1', 'body_place_id': '16', 'option_content': u'\u75bc\u75db'}, {'question_id': '1', 'option_id': '2', 'body_place_id': '17', 'option_content': u'\u9ebb\u6728'}, {'question_id': '1', 'option_id': '3', 'body_place_id': '18', 'option_content': u'\u65e0\u529b'}, {'question_id': '7', 'option_id': '18', 'body_place_id': None, 'option_content': u'\u6d3b\u52a8\u540e\u51cf\u8f7b'}, {'question_id': '8', 'option_id': '21', 'body_place_id': None, 'option_content': u'\u4f1a\u9634\u533a\u9ebb\u6728\uff0c\u5927\u5c0f\u4fbf\u5931\u7981\uff0c\u9633\u75ff'}, {'question_id': '8', 'option_id': '25', 'body_place_id': None, 'option_content': u'\u75bc\u75db\u4e0d\u4f34\u968f\u53d1\u70ed'}, {'question_id': '9', 'option_id': '29', 'body_place_id': None, 'option_content': u'\u662f'}, {'question_id': '11', 'option_id': '36', 'body_place_id': None, 'option_content': u'\u6309\u6469\u53f2'}, {'question_id': '7', 'option_id': '17', 'body_place_id': None, 'option_content': u'\u7ad9\u7acb\u52a0\u91cd\uff0c\u5f2f\u8170\uff08\u80fd\u9a91\u8f66\uff0c\u4e0d\u80fd\u884c\u8d70\uff09'}, {'question_id': '4', 'body_place_id': '14', 'option_content': '0-3-0'}], 'patient_name': u'\u9648\u7965748626784', 'id': ''}

print all_factors_request
all_disease = json.dumps(all_factors_request)
all_disease_with_age_older_than_50 = all_disease.replace('31','51')
print all_disease_with_age_older_than_50