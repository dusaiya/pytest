# encoding: utf-8
'''
Created on 2017年7月17日

@author: alibaba
'''
foutErr1=open('./final_sina_err_id','a')
##foutErr2=open('./final_sina_err_nouser','w')
foutInfo=open('./final_sina_info','a')
foutWeibo=open('./final_sina_ids','a')
for i in range(1,127):
    idxstr=str(i)
    print idxstr
    rightout = open("../../../../alldata/data4/uid_sina_right_" + idxstr, 'r')
    errorout = open("../../../../alldata/data4/uid_sina_error_" + idxstr, 'r')
    sinaout = open("../../../../alldata/data4/uid_sina_info_" + idxstr, 'r')
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
