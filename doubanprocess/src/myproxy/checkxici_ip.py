# encoding: utf-8
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib2
from myproxy.urlrequest import urlrequest




def proxyValidation(url, proxy):
    flag=False
    try:
        src = urlrequest(url, proxy, 1)
        result = src.read()
        if "159.226.43." in result:
            print proxy + ' explosured our ip!!!'
        else:
            print proxy + ' is a good ip!!!'
            flag=True
            return flag, proxy
    except urllib2.HTTPError as e:
        print proxy + ' got HTTP ERROR'
        print e
        return flag,proxy
    except Exception as e:
        print proxy + ' got OTHER ERROR'
        print e
        return flag,proxy


url="http://45.55.222.147:8899/dbyq/hello.htm"
fin=open('./xici_ip.txt','r')
fout=open('./goodxici_ip.txt','a')
for line in fin.readlines():
    proxy=line.replace("\n","")
    proxy="122.158.86.136:2467"
    flag,proxy=proxyValidation(url, proxy)
    if flag==True:
        fout.write(proxy.__str__()+'\n')
        fout.flush()

fout.close()
fin.close()





