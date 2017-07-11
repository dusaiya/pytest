# encoding: utf-8
'''
Created on 2017年7月11日

@author: alibaba
'''

import json
from douban import  douban_weibo

fin=open("../douban/uid_sina_id","r")
fout=open("./sina_domain2uid","w")
totalCt=0
for line in fin.readlines():
    userId, weiboIds = douban_weibo.line2str(line)
    data={"doubanId":userId,"weiboIds":""}
    correctList=[]
    errordata={"doubanId":userId,"weiboIds":""}
    errorList=[]
    errorCt=0
    for weiboId in weiboIds:
        weiboLine={"weiboId":weiboId,"uid":"","domain":""}
        try:
            if len(weiboId)<4:
                raise Exception("NOT_LONG_ENOUGH_ERROR")
            if douban_weibo.isAllNum(weiboId) & len(weiboId)>8: ##全是数字，长度超过
                weiboLine["uid"]=weiboId
            else:
                weiboLine["uid"]="123"
                weiboLine["domain"]=weiboId
            correctList.append(weiboLine)
        except Exception as err:  
            ##print weiboId+" is error"      
            errorList.append(weiboLine)
            errorCt=errorCt+1
    if len(correctList)>0:
        data["weiboIds"]=correctList
        data["msg"]="correct"
        fout.write(json.dumps(data))
    if errorCt>0:            
        errordata["weiboIds"]=errorList
        errordata["msg"]="error"
        fout.write(json.dumps(errordata))
    fout.write("\n")    
fin.close()
fout.close()
