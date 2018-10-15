#!/usr/bin/env python
# encoding: utf-8
# 生成每周列表

import time
import datetime
import pymongo
conn = pymongo.MongoClient()
db = conn.xmzp
post = db.jobs

today = datetime.date.today()
sevenday = datetime.timedelta(days=6)
lastweek = today - sevenday

# date = time.strftime("%Y-%m-%d", time.localtime())
num = post.find({"created_date":{"$gt":str(lastweek)}}).count()
res = post.find({"created_date":{"$gt":str(lastweek)}}).sort("start_date",pymongo.ASCENDING)

title = "一周招聘信息汇总 | "+str(lastweek)+"--"+str(today) + "(" + str(num) + "则)"

with open('./source/_posts/'+title+".md", 'w') as fo:
    fo.write("---\n")
    fo.write("title: "+title+"\n")
    fo.write("date: "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
    fo.write("tags: 一周招聘信息汇总\n")
    fo.write("---\n")
    fo.write("本周信息条数："+ str(num) +'   \U00002618 \n')
    fo.write("<!-- more -->\n\n")
    fo.write("| 截止时间 | 招聘人数 | 标题 | Url |\n| :-: | :-: | :-: | :-: |\n")
    for x in res:
        fo.write("| "+x['dead_time']+" | "+x['people']+" | "+x['title']+"|https://xmzp.weiweiblog.cn/"+"".join(x['created_date'].split('-'))+"/"+x['title']+"/ |\n")
    fo.write("![](https://cdn.weiweiblog.cn/20181015134814.png)")

print("一周招聘信息汇总编写完毕")
