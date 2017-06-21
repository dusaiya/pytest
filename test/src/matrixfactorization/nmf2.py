# encoding: utf-8
'''
Created on 2016年11月21日

@author: alibaba
'''
from numpy import * 

def load_data(file_path):
    f = open(file_path)
    V = []
    for line in f.readlines():
        lines = line.strip().split("\t")
        data = []
        for x in lines:
            data.append(float(x))
        V.append(data)
    return mat(V)

def train(V, r, k, e):
    m, n = shape(V)
    W = mat(random.random((m, r)))
    H = mat(random.random((r, n)))

    for x in xrange(k):
        #error 
        V_pre = W * H
        E = V - V_pre
        #print E
        err = 0.0
        for i in xrange(m):
            for j in xrange(n):
                err += E[i,j] * E[i,j]
        print err

        if err < e:
            break

        a = W.T * V
        b = W.T * W * H
        #http://blog.csdn.net/google19890102/article/details/51190313
        #乘法更新规则(multiplicative update rules) 保证非负
        for i_1 in xrange(r):
            for j_1 in xrange(n):
                if b[i_1,j_1] != 0:
                    H[i_1,j_1] = H[i_1,j_1] * a[i_1,j_1] / b[i_1,j_1]

        c = V * H.T
        d = W * H * H.T
        for i_2 in xrange(m):
            for j_2 in xrange(r):
                if d[i_2, j_2] != 0:
                    W[i_2,j_2] = W[i_2,j_2] * c[i_2,j_2] / d[i_2, j_2]

    return W,H 


if __name__ == "__main__":
    file_path = "./data1"

    V = load_data(file_path)
    W, H = train(V, 2, 100, 1e-5 )

    print V
    print W
    print H
    print W * H