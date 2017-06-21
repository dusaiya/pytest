# encoding: utf-8
# -*- coding: cp936 -*-
'''
Created on 2017年6月1日
豆瓣api
@author: alibaba
'''

import urllib2
## https://api.douban.com/v2/user/35661509

def doubanuser(name):
    url_prefix='https://api.douban.com/v2/user/'
    url=url_prefix+name
    req = urllib2.Request(url) # url 转换成发起get 请求的url  
    result = urllib2.urlopen(req) # 发起GET http服务  
    res = result.read()
    return res

'''
import httplib
##from douban_client import DoubanClient

url_prefix='https://api.douban.com/v2/user/'
name='35661509'
url=url_prefix+name
conn = httplib.HTTPConnection("180.163.189.113")
url='https://api.douban.com/v2/user/35661509'
conn.request(method="GET",url=url) 

response = conn.getresponse()
res= response.read()
print res
'''
