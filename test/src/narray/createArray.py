# encoding: utf-8
'''
Created on 2017年3月20日

@author: alibaba
'''

import numpy as np

a=np.arange(0,10,1) # 10不在结果里面
print a
b=np.linspace(0, 10, 11) #10 在结果里面
print b
c=np.logspace(0,2,5)
print c

# zeros(a.shape,a.type)= zeros_like(a)
#ones(),ones_like; empty,empty_like

#fromstring frombuffer fromfile
# fromfunction(func,shape)