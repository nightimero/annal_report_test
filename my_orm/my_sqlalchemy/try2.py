# -*- coding: utf-8 -*-
# from sqlalchemy import create_engine
#
# engine = create_engine("mysql+mysqldb://root:123456@localhost/test_tahiti")
#
# result = engine.execute("show tables;")
#
# res = result.fetchall()
#
# print res

from faker import Faker

fake = Faker("zh_CN")
print fake.ssn_with_age()