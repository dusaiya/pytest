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
fout = open("/home/align/code/douban_weibo/uid_sina_id_new_2", "a")
totalCt=0
for line in fin.readlines():
    totalCt+=1
    if (totalCt % 500) == 0:
         print totalCt
    userId, weiboIds = douban2dict.line2str(line)
    results = list(db.douban_weibo.find({'doubanId':userId}))
    if len(results) == 1:
         lineSize=len(weiboIds)
         dbSize=len(results[0]['weiboIds'])
         if lineSize>dbSize:
             print "doubanId" + userId + ";lineSize:" + str(lineSize)+ ";dbSize:" + str(dbSize)
             fout.write(line)
             fout.flush()         
fin.close() 
fout.close()  




