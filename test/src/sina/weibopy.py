#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
  
from weibo import APIClient  
import webbrowser #python内置的web框架
from __builtin__ import raw_input
import json
##import codecs
'''
appname:netTA17
App Key：2188666401
App Secret：9315033c6b91198e71881ed062bfdd49
授权回调页：http://www.csdn.net
取消授权回调页：http://www.csdn.net
code=b9ecda00b189a5b73e9d5aad8335b188
''' 
  
APP_KEY = '2188666401'  
APP_SECRET = '9315033c6b91198e71881ed062bfdd49'  
CALLBACK_URL = 'http://www.csdn.net'  
code='96d0c900c69a0b76cf4b39085d154997'  
  
#利用官方微博SDK  
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)  
#得到授权页面的url，利用webbrowser打开这个url  
url = client.get_authorize_url()  
##print url  
webbrowser.open_new(url)  
#获取code=后面的内容  
print '输入url中code后面的内容后按回车键：'  
code=raw_input() ##每次都要重新获取code(日了狗了)
r = client.request_access_token(code)  
access_token = r.access_token # 新浪返回的token，类似abc123xyz456  
expires_in = r.expires_in  
# 设置得到的access_token  
client.set_access_token(access_token, expires_in)  
  
#可以打印下看看里面都有什么东西  
print client.statuses__public_timeline()  

a=client.users.show.get(screen_name='霜盲')
te = json.dumps(a,ensure_ascii=False)
##tem = json.loads(te) 再次转换成json，并不需要
print a.location
##写文件
file = open('/Users/alibaba/Documents/workspace/python/test/src/sina/result.txt','w')
json.dump(a, file)
file.close()
##读文件
file = open('/Users/alibaba/Documents/workspace/python/test/src/sina/result.txt','r')
b = json.load(file)
file.close()

statuses = client.statuses__public_timeline()['statuses']  
length = len(statuses) 
#输出了部分信息  
for i in range(0,length):  
    print u'昵称：'+statuses[i]['user']['screen_name']  
    print u'简介：'+statuses[i]['user']['description']  
    print u'位置：'+statuses[i]['user']['location']  
    print u'微博：'+statuses[i]['text']  


