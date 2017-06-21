# encoding: utf-8
'''
Created on 2017年2月20日

@author: alibaba
'''
import numpy as np

 
a=np.array([1,2,3,4])
# print a
# print np.shape(a)
# print a.shape
a.shape=1,4
# print a
# print '--------'
b=np.array([[1,2,3,4],[5,6,7,8]])
# print b
# print b.shape
# print np.shape(b)
b.shape=4,-1  #-1 自动计算该维
# print b
# print b.shape
# print '--------'
c= b.reshape((8,1));
# print c
# print b
# b,c 依然共享同一个存储空间，修改其中一个矩阵，另外一个矩阵中的元素也将会被修改
# print '--------'
b[3,1]=71
# print c
# print b

# print c.dtype
set(np.typeDict.values())





