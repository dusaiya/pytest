# encoding: utf-8
'''
Created on 2017年7月19日

@author: alibaba
'''
from pymongo import MongoClient
import douban2dict
import json


def original_ids(db):
    '''
    原始uid录入更新，update形式，只更新一条记录
    '''
    fin=open("/Users/alibaba/Documents/workspace/python/pytest/doubanprocess/uid_sina_id","r")
    totalCt=0
    for line in fin.readlines():
        userId, weiboIds = douban2dict.line2str(line)
        dictData=douban2dict.doubanInfo2dict(userId, weiboIds)
        db.doubanInfo.update({'doubanId':userId},
                             {'$set':{'doubanId':userId},
                              '$addToSet':{'weiboIds':dictData['weiboIds']}},
                             upsert=True)
        totalCt+=1
    print totalCt
    fin.close()   
     
def infoInsert(db,fileName):
    fin=open(fileName,"r")
    totalCt=0
    for line in fin.readlines():
        db.weibo_info.save(json.loads(line))
        totalCt+=1
    print totalCt
    fin.close() 
    
def errInsert(db,fileName):
    fin=open(fileName,"r")
    totalCt=0
    for line in fin.readlines():
        db.err_info.save(json.loads(line))
        totalCt+=1
    print totalCt
    fin.close() 

def resultInsert(db,fileName):
    fin=open(fileName,"r")
    totalCt=0
    for line in fin.readlines():
        db.douban_weibo.insert(json.loads(line))
        totalCt+=1
    print totalCt
    fin.close() 
    
conn=MongoClient("10.200.6.7",27017)
db=conn.douban_weibo

##错误信息插入
fileName="/Users/alibaba/Documents/workspace/python/alldata/data6/final_sina_err"
##errInsert(db,fileName)

##正式信息
fileName="/Users/alibaba/Documents/workspace/python/alldata/data6/final_sina_ids"
resultInsert(db,fileName)

fileName="/Users/alibaba/Documents/workspace/python/alldata/data6/final_sina_info"
infoInsert(db,fileName)
