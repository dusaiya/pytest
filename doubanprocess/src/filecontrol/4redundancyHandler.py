# encoding: utf-8
'''
Created on 2017年7月20日

@author: alibaba
'''
from pymongo import MongoClient
conn=MongoClient("10.200.6.7",27017)
db=conn.douban_weibo

def redundancyRemove(db,doubanId):
    results=list(db.douban_weibo.find({'doubanId':doubanId}))
    basicRt=results[0]
    initCt=len(basicRt["weiboIds"])
    _id=basicRt["_id"]
    ct=0
    for result in results:
        ct+=1
        if ct==1:
            continue
        if initCt>=len(result["weiboIds"]):
            db.douban_weibo.remove({"_id":result["_id"]})
        else:
            db.douban_weibo.remove({"_id":basicRt["_id"]})
            basicRt=result
            initCt=len(basicRt["weiboIds"])
            _id=basicRt["_id"]
    
for redundancy in db.douban_ext.find():
    doubanId=redundancy["doubanId"].__str__()
    redundancyRemove(db,doubanId)
    db.douban_ext.remove({'doubanId':doubanId})       