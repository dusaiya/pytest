# encoding: utf-8
'''
Created on 2017年7月6日

@author: alibaba
'''
import sys
sys.path.append("..")
import douban_weibo
import myproxy.urlrequest as urlreq
import json
import time

def processHandler(idxstr,token,proxy):
    fin = open("./data/uid_sina_id_" + idxstr, 'r')
    rightout = open("./data/uid_sina_right_" + idxstr, 'a')
    errorout = open("./data/uid_sina_error_" + idxstr, 'a')
    sinaout = open("./data/uid_sina_info_", 'a')
    totalCt = 0
    for line in fin.readlines():
        userId, weiboIds = douban_weibo.line2str(line)
        data = {"doubanId":userId, "weiboIds":""}
        correctList = []
        errordata = {"doubanId":userId, "weiboIds":""}
        errorList = []
        errorCt = 0
        for weiboId in weiboIds:
            weiboLine = {"weiboId":weiboId, "uid":"", "domain":""}
            try:
                if len(weiboId) < 4:
                    raise Exception("NOT_LONG_ENOUGH_ERROR")
                if douban_weibo.isAllNum(weiboId) & (len(weiboId) > 8): ##全是数字，长度超过
                    src = urlreq.urlrequest(api_show(weiboId, token), proxy, 1)
                    html = src.read()
                    sinaout.write(html)
                    sinaout.write("\n")
                    sinaout.flush()
                    result = json.loads(html)
                    weiboLine["domain"] = result['domain'].__str__()
                    weiboLine["uid"] = result['idstr'].__str__()
                else:
                    src = urlreq.urlrequest(api_domain_show(weiboId, token), proxy, 1)
                    html = src.read()
                    sinaout.write(html)
                    sinaout.write("\n")
                    sinaout.flush()
                    result = json.loads(html)
                    weiboLine["domain"] = result['domain'].__str__()
                    weiboLine["uid"] = result['idstr'].__str__()
                correctList.append(weiboLine)
            except Exception as err:
                print err
                weiboLine["errMsg"] = err.__str__()
                errorList.append(weiboLine)
                errorCt = errorCt + 1
            time.sleep(10)
        if len(correctList) > 0:
            data["weiboIds"] = correctList
            data["msg"] = "correct"
            rightout.write(json.dumps(data))
            rightout.write("\n")
            rightout.flush()
        if errorCt > 0:
            errordata["weiboIds"] = errorList
            errordata["msg"] = "error"
            errorout.write(json.dumps(errordata))
            errorout.write("\n")
            errorout.flush()
        totalCt += 1
    print totalCt
    fin.close()
    rightout.close()
    errorout.close()
    sinaout.close()


def api_show(uid,token):
    uid_url="https://api.weibo.com/2/users/show.json" ##http://open.weibo.com/wiki/2/users/show
    url=uid_url+"?access_token="+token+"&uid="+uid
    return url

def api_domain_show(domain,token):
    domain_url="https://api.weibo.com/2/users/domain_show.json" ## http://open.weibo.com/wiki/2/users/domain_show
    url=domain_url+"?access_token="+token+"&domain="+domain
    return url

if __name__=="__main__":
    idxstr=sys.argv[1]
    token = '2.00UIuP3BzG7H5C23bacb5a88Sn8lXD' ## 根据weibotoken获取的token
    token = '2.00UIuP3BbB3mLDa89c08b4bdublSAC'
    proxy = '222.33.192.238:8118' ## goodxici_ip.txt
    processHandler(idxstr,token,proxy)
