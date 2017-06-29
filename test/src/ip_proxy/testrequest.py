import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib2

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url="http://45.55.222.147:8899/dbyq/hello.htm"
url="http://www.xicidaili.com/nn/10"
header = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }

try:
    response = requests.get(url, headers=header, timeout=10)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    print 'api error!'
    print response.text
    if "159.226.43.96" in response.text:
        print 'exposed our real ip !'
except Exception as e:
    print 'http error!'
    print e


'''
proxy_support = urllib2.ProxyHandler({'http':'http://%s' % proxy })   
opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)    
urllib2.install_opener(opener)
try:
  src = urllib2.urlopen(url, timeout=40)
  print src
except urllib2.HTTPError as e:
  logger.info(e)
except Exception as e:
  logger.info(e)
'''

