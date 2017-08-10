# encoding: utf-8
'''
Created on 2017年7月19日

@author: alibaba
'''
from pymongo import MongoClient
import douban2dict

conn = MongoClient("10.200.6.7", 27017)
db = conn.douban_weibo

fin = open("./uid_sina_id_new_2", "r")
fout = open("./uid_sina_id_new_3", "w")
totalCt=0
for line in fin.readlines():
    userId, weiboIds = douban2dict.line2str(line)
    result = list(db.douban_weibo.find({'doubanId':userId}))[0]
    dbObs=result["weiboIds"]
    dbSize=len(dbObs)
    dbWeiboIds=[]
    for dbOb in dbObs:
        dbWeiboIds.append(dbOb["weiboId"])
    for weiboId in weiboIds:
        if weiboId in dbWeiboIds:
            continue
        else:
            fout.write(line)
            fout.flush()
            break
fin.close() 
fout.close()  




