# coding:utf-8
from db import DB
from item import UserItem

db_ = DB()
print(db_.exists('user',1))

item = UserItem(1,'wupeng','20','2','2')
db_.save(item)