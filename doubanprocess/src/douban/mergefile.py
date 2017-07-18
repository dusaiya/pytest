# encoding: utf-8
'''
Created on 2017年7月17日

@author: alibaba
'''
foutId=open('./uid_sina_id','a')
foutErr1=open('./uid_sina_err_id','a')
##foutErr2=open('./uid_sina_err_nouser','a')
foutInfo=open('./uid_sina_info','a')
foutWeibo=open('./uid_sina_ids','a')
for i in range(1,50):
    idxstr=str(i)
    print idxstr
    fin = open("../douban/data/uid_sina_id_" + idxstr, 'r')
    rightout = open("../douban/data/uid_sina_right_" + idxstr, 'r')
    errorout = open("../douban/data/uid_sina_error_" + idxstr, 'r')
    sinaout = open("../douban/data/uid_sina_info_" + idxstr, 'r')
    ##ids
    lines=fin.readlines()
    foutId.writelines(lines)
    del lines
    ##正式结果
    lines=rightout.readlines()
    foutWeibo.writelines(lines)
    del lines
    ##错误结果
    lines=errorout.readlines()
    foutErr1.writelines(lines)
    del lines
    ##微博信息
    lines=sinaout.readlines()
    foutInfo.writelines(lines)
    del lines
    
foutWeibo.close()
foutInfo.close()
foutErr1.close()
##foutErr2.close()
foutId.close()
