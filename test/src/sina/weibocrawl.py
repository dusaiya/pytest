# encoding: utf-8
'''
Created on 2017年5月4日

@author: alibaba
'''

from weibo import APIClient  
import webbrowser #python内置的web框架
from __builtin__ import raw_input
import json
import time
import random

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
expires_in = r.expires_in  
# 设置得到的access_token  
client.set_access_token(access_token, expires_in)  
  

fin=open('./loss_nick_freq_sorted.txt','r')
fout=open('./nick_result.txt','a')
ferr=open('./nick_err.txt','a')
frecord=open('./nick_record.txt','a')
count=0
for line in fin.readlines(): 
    ##if(count>270):
    ##    break
    count+=1
    if( count<=20): ##跳过上次爬过的行数
        continue
    
    name,num=line.split('\t',1) #分割一次

    try:
        a=client.users.show.get(screen_name=name) ##获取 users/show接口
        te = json.dumps(a) ##处理unicode
        ##json.dump(te, fout)
        fout.write(te+'\n')
        frecord.write(str(count)+'--'+name +':success.\n')
    except Exception as err:
        frecord.write(str(count)+'--'+name +':'+str(err.__str__)+'\n')
        ferr.write(line)
    time.sleep(10+random.randint(0,10))
'''    
    try:
        a=client.users.show.get(screen_name=name) ##获取 users/show接口
        te = json.dumps(a) ##处理unicode
        ##json.dump(te, fout)
        fout.write(te+'\n')
        print str(count)+'--'+name +':success.'
    except Exception as err:  
        print str(count)+'--'+name +':err!'
        ferr.write(line)
        
    time.sleep(5+random.randint(0,10)) ##等待时间
'''
fin.close()
fout.close()
ferr.close()
frecord.close()

