#!/usr/bin/env python
# encoding: utf-8
import time
import pymongo
conn = pymongo.MongoClient()
db = conn.xmzp
post = db.jobs
date = time.strftime("%Y-%m-%d", time.localtime())
res = post.find({"created_date":date}).sort("start_date",pymongo.ASCENDING)
num = 0
for x in res:
    num += 1
    with open('./source/_posts/'+x['title']+".md", 'w') as fo:
        fo.write("---\n")
        fo.write("title: "+x['title']+'\n')
        fo.write("date: "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
        fo.write("tags: "+x['tag']+'\n')
        fo.write("---\n")
        fo.write("发布时间："+ x['start_date']+'   \U0001F31F   招聘人数：'+x['people']+'   \U0001F308   截止时间：'+x['dead_time']+'\n')
        fo.write("<!-- more -->\n")
        fo.write(x['content'])
        fo.write("![](https://cdn.weiweiblog.cn/20181015134257.png)")
        time.sleep(1)
print("添加"+str(num)+"篇文章")

