#!/usr/bin/env python
# encoding: utf-8

import pymongo
conn = pymongo.MongoClient()
db = conn.xmzp
post = db.jobs
post.ensure_index([("url", pymongo.ASCENDING)], unique=True)

#data = [
#    {'url':'123', 'title':'aaa'},
#    {'url':'124', 'title':'bbb'},
#    {'url':'125', 'title':'ccc'},
#    {'url':'126', 'title':'ddd'},
#    {'url':'123', 'title':'eee'},
#    {'url':'127', 'title':'ok'},
#]
#try:
#    post.insert(data, continue_on_error=True)
#    #post.insert_many(data, ordered=False)
#except pymongo.errors.DuplicateKeyError:
#    pass
