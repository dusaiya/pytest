# encoding: utf-8
'''
Created on 2017年7月6日

@author: alibaba
'''
import ValidException
import douban_weibo

'''
'''
fin = open("./uid_sina_id", 'r')
rightout=open("./uid_sina_id_right", 'a')
errorout=open("./uid_sina_id_error", 'a')
for line in fin.readlines():
    userId, weiboIds = douban_weibo.line2str(line)
    for weiboId in weiboIds:
        try:
            if len(weiboId)<4:
                raise ValidException(ValidException.NOT_LONG_ENOUGH_ERROR,'weiboId\'s length is less then 4')
            if douban_weibo.isAllNum(weiboId) & len(weiboId)>8: ##全是数字，长度超过
                rightout.write(userId)
        except ValidException as err:        
            errorout.write(userId)
fin.close()
rightout.close()
errorout.close()

