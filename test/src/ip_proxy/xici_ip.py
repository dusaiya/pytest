# encoding: utf-8
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import time


def filter_speed(self,speed):
    speed = speed.replace(u'秒','')
    return float(speed)

def filter_life(self,life):
    '''
                    过滤存活时间
    '''
    life = life.replace(u'天','')
    return life

def is_valid_time(self,life):
    '''
                    判断是否是有效的时间
    '''
    if life.rfind(u'分')>=0 or life.rfind(u'时')>=0:
        return False
    else:
        return True  


def responseHandler(trs,file):
    if trs:
        for i in range(1,len(trs)):
        ##for i in range(1, 2):
            tr = trs[i]
            tds = tr.select('td')
            ##print tds
            td = tds[1]
            ##print td.__class__
            content1 = td.string
            ##print content1.__class__
            ipmsg1 = tds[1].string + ':' + tds[2].string + '\t' + tds[8].string
            ##file.write(ipmsg1)
            ##file.flush()
            ##print ipmsg1.__class__
            print ipmsg1
            ipmsg2 = tds[6].div.div.get('style')
            ##print ipmsg2.__class__
            ##print ipmsg2

def get_proxy_msg(url):
    proxy='125.77.80.118:808'
    proxies = {"https": "https://{proxy}".format(proxy=proxy)}
    try:
        ##response = requests.get(url, headers=header, proxies=proxies, timeout=40)
        response = requests.get(url, headers=header,  timeout=40)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup=BeautifulSoup(response.text,"xml")
        trs = soup.table.select('tr')
        return trs
    except Exception as e:
        print 'http error!'
        print e
    return

##基本蚕食
baseurl="http://www.xicidaili.com/nn/"
header = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }
file=open('./xici_ip.txt','a+')

#开启流程
url=baseurl
for i in range(1,10):
    url=baseurl+str(i)
    print url
    trs=get_proxy_msg(url)
    responseHandler(trs,file)
    time.sleep(10)
file.close()


