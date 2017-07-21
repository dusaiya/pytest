# encoding: utf-8
'''
Created on 2017年7月6日

@author: alibaba
'''
import sys
sys.path.append("..")
import threading
import douban_weibo
import urlrequest as urlreq
import json
import time
import datetime

def processHandler(idxstr, token, proxy):
    fin = open("./data/uid_sina_id_" + idxstr, 'r')
    rightout = open("./data/uid_sina_right_" + idxstr, 'a')
    errorout = open("./data/uid_sina_error_" + idxstr, 'a')
    sinaout = open("./data/uid_sina_info_" + idxstr, 'a')
    logout = open("./data/uid_sina_log_" + idxstr, 'a')
    totalCt = 0
    for line in fin.readlines():
        userId, weiboIds = douban_weibo.line2str(line)
        now = datetime.datetime.now()
        logout.write('[' + now.__str__() + '] Handling the' + str(totalCt) + 'th [DoubanId]:' + userId + '\n')
        data = {"doubanId":userId, "weiboIds":""}
        correctList = []
        errordata = {"doubanId":userId, "weiboIds":""}
        errorList = []
        errorCt = 0
        for weiboId in weiboIds:
            logout.write('Handling [DoubanId]:' + userId + ';[weibo]:' + weiboId + '\n')
            weiboLine = {"weiboId":weiboId, "uid":"", "domain":""}
            try:
                if len(weiboId) < 4:
                    raise Exception("NOT_LONG_ENOUGH_ERROR")
                if douban_weibo.isAllNum(weiboId) & (len(weiboId) > 8):  # #全是数字，长度超过
                    logout.write('INFO for [DoubanId]:' + userId + ';[weibo]:' + weiboId + ", geting Sina [UID].\n")
                    logout.flush()
                    src = urlreq.urlrequest(api_show(weiboId, token), proxy, 0)
                    html = src.read()
                    sinaout.write(html)
                    sinaout.write("\n")
                    sinaout.flush()
                    result = json.loads(html)
                    weiboLine["domain"] = result['domain'].__str__()
                    weiboLine["uid"] = result['idstr'].__str__()
                else:
                    logout.write('INFO for [DoubanId]:' + userId + ';[weibo]:' + weiboId + ', geting Sina [Domain].\n')
                    logout.flush()
                    src = urlreq.urlrequest(api_domain_show(weiboId, token), proxy, 0)
                    html = src.read()
                    sinaout.write(html)
                    sinaout.write("\n")
                    sinaout.flush()
                    result = json.loads(html)
                    weiboLine["domain"] = result['domain'].__str__()
                    weiboLine["uid"] = result['idstr'].__str__()
                correctList.append(weiboLine)
            except Exception as err:
                errMsg = err.__str__()
                logout.write('ERROR in [DoubanId]:' + userId + ';[weibo]:' + weiboId + '.')
                logout.write('[ERROR_MSG]:' + errMsg + ". \n")
                logout.flush()
                weiboLine["errMsg"] = errMsg
                errorList.append(weiboLine)
                errorCt = errorCt + 1
                if 'Forbidden' in errMsg:
                    time.sleep(1800)
            time.sleep(60)
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
        if (totalCt % 50) == 49:
            time.sleep(600)  ##休息
    fin.close()
    rightout.close()
    errorout.close()
    sinaout.close()
    logout.close()


def api_show(uid, token):
    uid_url = "https://api.weibo.com/2/users/show.json"  # #http://open.weibo.com/wiki/2/users/show
    url = uid_url + "?access_token=" + token + "&uid=" + uid
    return url

def api_domain_show(domain, token):
    domain_url = "https://api.weibo.com/2/users/domain_show.json"  # # http://open.weibo.com/wiki/2/users/domain_show
    url = domain_url + "?access_token=" + token + "&domain=" + domain
    return url

if __name__ == "__main__":
    token_list=['2.00UIuP3BzG7H5C23bacb5a88Sn8lXD','2.00UIuP3BbB3mLDa89c08b4bdublSAC', ##01
       '2.00UIuP3Briwt6Cb0f12452e00kANPh','2.00UIuP3B0Ra6U20b5467ecf1CRez_E',
       '2.00UIuP3BwrQ9FB1a32521cbeZCGnPE','2.00UIuP3BFWAm8E79403803c30Z9BlM',
       '2.00UIuP3BeZTRQBd83a059cf80Qen4n','2.00UIuP3B06UWubdabfdd74d5woouOE',
       '2.00UIuP3BI5YQeD1d95b25a27Pr3JmC','2.00UIuP3BQxo2LCcc0f7325f3tadvPB',
       '2.00NEMetGay_FFBbc52958f4difW5OC','2.00NEMetGaRlCXCdddf3906a5tPdzFD',##02
       '2.00NEMetGsMmgODcd28e420000NmFLw','2.00NEMetGmuJzWC4aeba2485cGsJYoB',
       '2.00NEMetGfeDE_Ce6935c6064miSZ8E','2.00NEMetGNCkgiD7707de324eVlbMWD',
       '2.00NEMetG0kuZwn1b4c1d3cdeBPO8WD','2.00NEMetG03IIHu6948de5f52ZNOSFC',
       '2.00NEMetGfXLBaC9256ee0202tvFLME','2.00NEMetGwc3mGD26f955ec93i3CRSB',
       '2.00LCBusCN2WTLBbed61de5420XGIVR','2.00LCBusC1slZYD708b15a0ad0svBNk',##03
       '2.00LCBusC0PIkiH83aba463dc2pqcSC','2.00LCBusCsZFyWE52970e5eb0uSGVPD',
       '2.00LCBusCMW34pB253bcbc2b4BjYTdE','2.00LCBusC4fiiLBf433c67bf1B6vMcC',
       '2.00LCBusC0muGiZaffef56b9a0JtOn6','2.00LCBusCGY_p9E58b3714882HPzV_C',
       '2.00LCBusCblSFmC330cc1ea3bgTzLlC','2.00LCBusC0tdUwYbe9e603934JlzlCD',
       '2.00d2PwWCKXRDdC5606d3e3c2w_qd7D','2.00d2PwWCAG4DRD5459836577D5A4lC',##04
       '2.00d2PwWCDNqgHC6ade683ee9kEm9GC','2.00d2PwWCSN1EDB5c11c68808nUs6SC',
       '2.00d2PwWC08H18Na105709e0ehvZGZC','2.00d2PwWCemaTYCce7b3565760idYVS',
       '2.00d2PwWC0zcijg74bd1db8e9LJKq6B','2.00d2PwWChZoOPC710033d0edND8odE',
       '2.00d2PwWCjDEY5Bf2e631900908Tk8d','2.00d2PwWCgnvtSC205404068aVw5lxC']
    idxstr = sys.argv[1]
    tokenidx = sys.argv[2]
    token = token_list[int(tokenidx) - 1]
    proxy = '222.33.192.238:8118'  # # goodxici_ip.txt
    ##t1 = threading.Thread(target=processHandler, args=(idxstr, token, proxy))
    processHandler(idxstr, token, proxy)
    '''
    '''
    threads = []
    for i in range(0,10):
        idxstr=str(int(idxstr)+i)
        tokenidx=str(int(tokenidx)+i)
        token = token_list[int(tokenidx)]
        proxy = '222.33.192.238:8118'  # # goodxici_ip.txt
        t1 = threading.Thread(target=processHandler,args=(idxstr, token, proxy))
        threads.append(t1)
        ##processHandler(idxstr, token, proxy)
    for t in threads:
        t.setDaemon(True)
        t.start()
        print "all over %s" %time.ctime()
    
