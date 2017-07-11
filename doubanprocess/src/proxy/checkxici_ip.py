# encoding: utf-8
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib2
from proxy.urlrequest import urlrequest




def proxyValidation(url, proxy):
    try:
        src = urlrequest(url, proxy, 1)
        html = src.read()
        if "159.226.43." in html:
            print proxy + ' explosured our ip!!!'
        else:
            print proxy + ' is a good ip!!!'
    except urllib2.HTTPError as e:
        print proxy + ' got HTTP ERROR'
        print e
    except Exception as e:
        print proxy + ' got OTHER ERROR'
        print e


url="http://45.55.222.147:8899/dbyq/hello.htm"
fin=open('./xici_ip.txt','r')
for line in fin.readlines():
    proxy=line.replace("\n","")
    proxyValidation(url, proxy)
fin.close()





