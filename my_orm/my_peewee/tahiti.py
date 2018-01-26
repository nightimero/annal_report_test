# -*- coding: utf-8 -*-
from peewee import *
from playhouse.db_url import connect
from datetime import datetime

# 两种方式连接数据库。


# mysql_db = MySQLDatabase(host="localhost", port=3306, user="root", passwd="123456", database='test_tahiti')
#
# mysql_db.connect()  # 连接数据库

mysql_db = connect("mysql://root:123456@localhost:3306/test_tahiti")


class BaseModel(Model):
    class Meta:
        database = mysql_db


class Locations(BaseModel):
    location_id = PrimaryKeyField()
    location_name = CharField()


# If you want to explicitly specify a column, use db_column:
class Units(BaseModel):
    unit_id = PrimaryKeyField()
    unit_num = IntegerField()
    # db_colum 会改变在数据库中该字段的名称。
    location_id = ForeignKeyField(Locations, db_column='location_name', related_name='units')


class Question1(BaseModel):
    # undeclared 就是不在数据库中创建。
    # survey_id = BigIntegerField(undeclared=True)
    # constraints = None - a list of one or more constraints, e.g. [Check('price > 0')]
    # survey_id = BigIntegerField(constraints=)
    survey_id = BigIntegerField(default=1)
    question_type = SmallIntegerField(default=1)
    question_content = CharField()
    is_required = SmallIntegerField(default=1)
    remark = CharField()
    create_time4 = DateTimeField(default=datetime.utcnow)






mysql_db.drop_tables([Question1, Locations, Units])
mysql_db.create_tables([Question1, Locations, Units])

print mysql_db.get_conn()  # 获取数据库连接
mysql_db.close()
