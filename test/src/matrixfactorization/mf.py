# encoding: utf-8
'''
Created on 2016年11月16日

@author: alibaba
'''

import numpy  
#alpha beta 两个方向的不同步长
# <herf>http://blog.csdn.net/shubingzhuoxue/article/details/51006004</herf> 梯度求导的求解
def matrix_factorisation(Original, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):  
    Q = Q.T  
    for step in xrange(steps):  
        for i in xrange(len(Original)):  
            for j in xrange(len(Original[i])):  
                if Original[i][j] > 0:  #0表示是空缺值, 不进行修正
                    eij = Original[i][j] - numpy.dot(P[i,:],Q[:,j])  
                    for k in xrange(K):  #梯度下降更新
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])  
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])  
        eR = numpy.dot(P,Q) 
        #计算累计误差判断是否跳出 
        e = 0  
        m,n=Original.shape
        for i in xrange(m):  
            for j in xrange(n):  
                if Original[i][j] > 0:  
                    e = e + pow(Original[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)  
                    for k in xrange(K):  
                        e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))  
        if e < 0.001:  
            break  
    return P, Q.T  

R = [  
     [5,3,0,1],  
     [4,0,0,1],  
     [1,1,0,5],  
     [1,0,0,4] 
    ]  
   
R = numpy.array(R)  
   
N1 = len(R)  
M = len(R[0])  
K = 4
   
P = numpy.random.rand(N1,K)  
Q = numpy.random.rand(M,K)  
   
nP, nQ = matrix_factorisation(R, P, Q, K,steps=5000)  
nR = numpy.dot(nP, nQ.T)  
print(R)
print(numpy.dot(nP, nQ.T))
#numpy.linalg.svd(a, full_matrices, compute_uv)
#还原后的矩阵跟原矩阵很接近，并且对原来空缺的值作出了预测。
# nP, nQ = matrix_factorisation(R, P, Q, K,steps=50000)  
# nR = numpy.dot(nP, nQ.T)  
# print(numpy.dot(nP, nQ.T))
