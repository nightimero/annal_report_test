# -*- coding:utf-8 -*-
from sqlalchemy import Column,String,create_engine,MetaData,Table,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test',echo=True)

# finish：这样为什么不行？ 因为创建表的方式不同。类似下面创建方式
metadata = MetaData(engine)
people = Table('people',metadata,
               Column('id',Integer,primary_key=True),
               Column('name',String(50)),
               Column('fullname',String(100))
)
metadata.create_all()
#
Base.metadata.create_all(engine)
DbSession = sessionmaker(bind=engine)

session = DbSession()

jake = User(id='6', name='jake')

session.add(jake)

session.commit()

session.close()
