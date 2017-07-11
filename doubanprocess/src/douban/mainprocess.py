# encoding: utf-8
'''
Created on 2017年7月6日

@author: alibaba
'''
import douban_weibo
import myproxy.urlrequest as urlreq
import json

def api_show(uid,token):
    uid_url="https://api.weibo.com/2/users/show.json" ##http://open.weibo.com/wiki/2/users/show
    url=uid_url+"?token="+token+"&uid="+uid
    return url

def api_domain_show(domain,token):
    domain_url="https://api.weibo.com/2/users/domain_show.json" ##http://open.weibo.com/wiki/2/users/domain_show
    url=domain_url+"?token="+token+"&domain="+domain
    return url

token='2.00UIuP3BzG7H5C23bacb5a88Sn8lXD' ## 根据weibotoken获取的token
proxy='112.85.208.91:808' ## goodxici_ip.txt

fin = open("./uid_sina_id_test", 'r')
rightout=open("./uid_sina_id_right_test", 'a')
errorout=open("./uid_sina_id_error_test", 'a')

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
                src=urlreq.urlrequest(api_domain_show(weiboId,token), proxy, 1)
                print src
                print src.__class__
                weiboLine["domain"]=weiboId
            correctList.append(weiboLine)
        except Exception as err:  
            ##print weiboId+" is error"      
            errorList.append(weiboLine)
            errorCt=errorCt+1
    if len(correctList)>0:
        data["weiboIds"]=correctList
        data["msg"]="correct"
        rightout.write(json.dumps(data))
        rightout.write("\n")
    if errorCt>0:            
        errordata["weiboIds"]=errorList
        errordata["msg"]="error"
        errorout.write(json.dumps(errordata))
        errorout.write("\n")    
    totalCt+=1
    if totalCt>1:
        break
fin.close()
rightout.close()
errorout.close()

