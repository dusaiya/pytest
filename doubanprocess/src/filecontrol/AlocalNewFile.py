# encoding: utf-8
'''
Created on 2017年7月19日
因为高网络开销，尽可能在服务器上运行
@author: alibaba
'''
from pymongo import MongoClient
import douban2dict

conn = MongoClient("localhost", 27017)
db = conn.douban_weibo

fin = open("/home/align/code/douban_weibo/uid_sina_id", "r")
fout = open("/home/align/code/douban_weibo/uid_sina_id_new_1", "a")
totalCt=0
for line in fin.readlines():
    totalCt+=1
    if (totalCt % 500) == 0:
         print totalCt
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




