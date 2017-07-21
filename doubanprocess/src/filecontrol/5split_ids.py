# encoding: utf-8
'''
Created on 2017年7月13日

@author: alibaba
'''
fin = open("/Users/alibaba/Documents/workspace/python/pytest/doubanprocess/uid_sina_id_new", 'r')
fileCt=0 ##从0开始命名
totalCt=1
fout=open("/Users/alibaba/Documents/workspace/python/alldata/data/uid_sina_id_"+str(fileCt),'w')
for line in fin.readlines():
    totalCt+=1
    fout.write(line)
    fout.flush()
    if totalCt==151:
        fout.close()
        totalCt=1
        fileCt+=1
        fout=open("/Users/alibaba/Documents/workspace/python/alldata/data/uid_sina_id_"+str(fileCt),'w')
fout.close()
fin.close()
