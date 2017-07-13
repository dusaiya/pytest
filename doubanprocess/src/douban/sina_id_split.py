# encoding: utf-8
'''
Created on 2017年7月13日

@author: alibaba
'''
fin = open("./uid_sina_id", 'r')
fileCt=1
totalCt=1
fout=open("./data/uid_sina_id_"+str(fileCt),'w')
for line in fin.readlines():
    totalCt+=1
    fout.write(line)
    fout.flush()
    if totalCt==2001:
        fout.close()
        totalCt=1
        fileCt+=1
        fout=open("./data/uid_sina_id_"+str(fileCt),'w')
fout.close()
fin.close()