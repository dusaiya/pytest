# encoding: utf-8
'''
Created on 2017年3月27日

@author: alibaba
'''

import numpy as np
from numpy.lib.stride_tricks import as_strided


def make_data(M, N, noise_scale):
    x = np.random.standard_normal(M)
    h = np.random.standard_normal(N)
    
    y = np.convolve(x, h)
    yn= y + np.random.standard_normal(len(y)) * noise_scale * np.max(y)    
    return x, yn, h



def solve_h(x, y, N):
    X = as_strided(x, shape=(len(x)-N+1, N), strides= (x.itemsize, x.itemsize))
    Y =y[N-1:len(x)]
    h = np.linalg.lstsq(X,Y)
    return h[0][::-1]


x, yn, h= make_data(1000,100,0.4)
H=solve_h(x, yn, 120)
H2=solve_h(x,yn,80)

print H.shape
print H2.shape


