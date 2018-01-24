# -*- coding:utf-8 -*-
from peewee import *
from playhouse.sqlite_ext import SqliteDatabase
import datetime

db = SqliteDatabase('my_database.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now())
    is_published = BooleanField(default=True)


db.connect()
# db.drop_tables([User, Tweet])
# db.create_tables([User, Tweet])

# charlie = User.create(username='charlie')
# huey = User(username='huey')
# huey.save()
#
# Tweet.create(user=charlie, message='My first Tweet')

print User.get(User.username == 'charlie').username

usernames = ['charlie', 'huey', 'mickey']
users = User.select().where(User.username << usernames)
usernames_in_table = [user.username for user in users]
print usernames_in_table
tweets_v0 = Tweet.select().where(Tweet.user << users)
messages = [tweet.message for tweet in tweets_v0]
print messages
tweets_v1 = Tweet.select().join(User).where(User.username << usernames)
print [(tweet.message, tweet.created_date.strftime('%Y%m%d %H:%M:%S'),
        tweet.user.username, tweet.user.id) for tweet in tweets_v1]

db.close()
