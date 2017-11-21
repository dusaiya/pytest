# encoding: utf-8
'''
Created on 2017年7月13日

@author: alibaba
'''
directName = "data12"
fileSize = 200
fin = open("/Users/alibaba/Documents/workspace/python/alldata/" + directName + "/uid_sina_id_undone", 'r')
fileCt = 0  # #从0开始命名
totalCt = 1
fout = open("/Users/alibaba/Documents/workspace/python/alldata/" + directName + "/uid_sina_id_" + areastr(fileCt), 'w')
for line in fin.readlines():
    totalCt += 1
    fout.write(line)
    fout.flush()
    if totalCt == fileSize + 1:
        fout.close()
        totalCt = 1
        fileCt += 1
        fout = open("/Users/alibaba/Documents/workspace/python/alldata/" + directName + "/uid_sina_id_" + areastr(fileCt), 'w')
fout.close()
fin.close()
