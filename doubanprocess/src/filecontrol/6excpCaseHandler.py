# encoding: utf-8
'''
Created on 2017年7月21日

@author: alibaba
'''

from pymongo import MongoClient
import douban2dict

conn = MongoClient("10.200.6.7", 27017)
db = conn.douban_weibo

directName = "data7"
fin = open("/Users/alibaba/Documents/workspace/python/alldata/" + directName + "/final_sina_id", "r")
fout = open("/Users/alibaba/Documents/workspace/python/alldata/" + directName + "/uid_sina_id_new", "w")
for line in fin.readlines():
    userId, weiboIds = douban2dict.line2str(line)
    results = list(db.douban_weibo.find({'doubanId':userId}))
    if len(results) == 1:
        continue
    if len(results) == 0:
        fout.write(line)
        fout.flush()
    if len(results) > 1:
        db.douban_ext.insert({'doubanId':userId})
fin.close() 
fout.close()  

