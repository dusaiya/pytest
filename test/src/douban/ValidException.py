# encoding: utf-8
'''
Created on 2017年7月6日

@author: alibaba
'''
NOT_LONG_ENOUGH_ERROR="NOT_LONG_ENOUGH_ERROR"
'''
长度不够错误
'''
    
NOT_ALL_NUM="NOT_ALL_NUM"
'''
并不全是数字字母
'''
    
class ValidException(Exception):
    '''
    classdocs
    用户微博账号验证异常类
    '''
    
    def __init__(self, errorCode,errorMsg):
        '''
        Constructor
        '''
        self.errorCode=errorCode
        self.errorMsg=errorMsg
    
        
    def errCode(self):
        '''
        '''
        return self.errorCode
    
    
    def errMsg(self):
        return self.errorMsg
    

