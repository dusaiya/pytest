# encoding: utf-8
'''
Created on 2017年10月25日

@author: alibaba
'''
import sys
sys.path.append("../")
import douban.urlrequest as urlreq

def api_show(uid, token):
    uid_url = "https://api.weibo.com/2/users/show.json"  # #http://open.weibo.com/wiki/2/users/show
    url = uid_url + "?access_token=" + token + "&uid=" + uid
    return url


weiboId="1849257892"
weiboId="5157812575"
token='2.00d2PwWC08H18Na105709e0ehvZGZC'
proxy=""
src = urlreq.urlrequest(api_show(weiboId, token), proxy, 0)
html = src.read()
print html
