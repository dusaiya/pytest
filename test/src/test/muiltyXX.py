# encoding: utf-8
'''
Created on 2017年7月16日

@author: alibaba
'''
import threading
from time import ctime,sleep


def music(ar1,ar2):
    for i in range(10):
        print "I was listening to %s. %s" %(ar1,ar2)
        sleep(10)

def move(ar1,ar2):
    for i in range(2):
        print "I was at the %s! %s" %(ar1,ar2)
        sleep(5)

threads = []
for i in range(0,10):
    print i
    ar1='0'
    ar2='10'
    ar1=str(int(ar1)+i)
    ar2=str(int(ar2)+i)
    t1 = threading.Thread(target=music,args=(ar1,ar2))
    threads.append(t1)


if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    print "all over %s" %ctime()