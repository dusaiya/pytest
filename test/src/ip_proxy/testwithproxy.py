# encoding: utf-8
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib2
##url = "https://api.douban.com/v2/user/136846329"
##url="http://10.60.1.92:8899/dbyq/hello.htm"
##url="http://ip-api.com/json"
##url="http://edns.ip-api.com/json"
##url="http://api.ip138.com/query/?datatype=jsonp&token=12c7d20ac7a65f85e98f8ddb3753a588"
##url="https://www.baidu.com"
def urlrequest(url, proxy,flag):
    if(flag):
        proxy_support = urllib2.ProxyHandler({'http':'http://%s' % proxy})
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        request = urllib2.Request(url)
        src = urllib2.urlopen(request, timeout=40)
    else:
        request = urllib2.Request(url)
        src = urllib2.urlopen(request, timeout=40)
    return src



'''
url="http://45.55.222.147:8899/dbyq/hello.htm"
url="http://www.xicidaili.com/nn/1"
headers={'user': 'Mozilla/5.0'}
headers = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }
proxy='103.206.253.90:8080'
proxy='183.131.19.233:808'  ##nb proxy ip
proxy='37.32.19.245:80'

try:
    src = urlrequest(url, proxy,1)
    html = src.read()
    print html
    if "159.226.43." in html:
        print 'ip exploded!!!'
    print 'finished'
except urllib2.HTTPError as e:
    print 'HTTP ERROR'
    print e
except Exception as e:
    print 'OTHER ERROR'
    print e
'''

'''
94.177.240.13:1189
37.32.19.245:80   ###优秀的高匿ip
125.77.80.118:808 ###优秀的高匿ip
'''