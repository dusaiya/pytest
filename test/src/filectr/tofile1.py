# encoding: utf-8
'''
Created on 2017年3月28日

@author: alibaba
'''

import numpy as np

a = np.arange(0,12)
a.shape=3,4
print a

'''
## 第一组实验 直接存取C++语言(默认)格式数据, 但是不带格式
a.tofile("a.bin")

b=np.fromfile("a.bin",dtype=np.int32)
print b

b=np.fromfile("a.bin",dtype=np.float)
print b

b=np.fromfile("a.bin",dtype= np.int64)
print b 
'''

'''
## 使用 save load 会自动处理格式
np.save("a.npy",a)
c=np.load("a.npy")
print c
存储多个可以用 savez("file.npz",a,b,name3=c)
result=load("file.npz")
result["arr_1"] a
result["arr_2"] b
result["name3"] c
'''

'''
#实验三 txt 文件存储 
c=np.arange(0,12,0.5).reshape(4,-1)
print c
print '----------------'
np.savetxt("c.txt", c) ## 默认按照 '%.18e'格式 存储数据
m=np.loadtxt("c.txt")
print m
np.savetxt("d.txt", c, fmt="%d", delimiter=",") ##指定格式和分隔符
m=np.loadtxt("d.txt",delimiter=",")
print m
'''

'''
##csv文件处理, 处理目录等信息
指定结构数据类型
persontype=np.dtype({
    'names':['name','age','weight','height'],
    'formats':['S32','i', 'f', 'f']})
f=file("test.csv")
f.readline()
data=np.loadtxt(f,delimiter=",", dtype=persontype)
'''

'''
通过文件对象, 对npy文件存取多个数组
f=file("test.npy","wb")
np.save(f,a) ## 存储三个不同的数组
np.save(f,a+1)
np.save(f,a+2)
f.close()

f=file("test.npy","rb")
np.load(f)          ## 获取 a
np.load(f)          ## 获取 a+1
np.load(f)          ## 获取 a+2

'''




