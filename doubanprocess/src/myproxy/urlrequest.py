# encoding: utf-8
import urllib2

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


