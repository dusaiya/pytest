# encoding: utf-8
'''
Created on 2017年7月11日

@author: alibaba
'''
import json
from douban import  douban_weibo

fin=open("../douban/uid_sina_id","r")
fout=open("./sina_domain2uid","a")

line=fin.readline()
print line
userId, weiboIds = douban_weibo.line2str(line)
data={"doubanId":userId,"weiboIds":""}
print data
fout.write(json.dumps(data))
correctList=[]
for weiboId in weiboIds:
    weiboLine={"weiboId":weiboId,"uid":"","domain":""}
    
    
fin.close()
fout.close()
