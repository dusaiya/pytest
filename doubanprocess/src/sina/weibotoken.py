# encoding: utf-8
'''
Created on 2017年5月4日

@author: alibaba
'''

from weibo import APIClient  
import webbrowser #python内置的web框架
from __builtin__ import raw_input
import time

APP_KEY = '2188666401'  
APP_SECRET = '9315033c6b91198e71881ed062bfdd49'  
CALLBACK_URL = 'http://www.csdn.net'  
##code='96d0c900c69a0b76cf4b39085d154997'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()  
webbrowser.open_new(url)  
print '输入url中code后面的内容后按回车键：'  
code=raw_input()
r = client.request_access_token(code)  
access_token = r.access_token # 新浪返回的token，类似abc123xyz456  
print access_token.__class__
print access_token
expires_in = r.expires_in 
print  expires_in.__class__
print expires_in
