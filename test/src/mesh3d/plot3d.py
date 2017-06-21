# encoding: utf-8
'''
Created on 2016年12月27日

@author: alibaba
'''
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
N1=300
normA1 = np.random.normal(0.2,0.03,size=N1)   
normA2 = np.random.normal(0.5,0.03,size=N1) 
from mpl_toolkits.mplot3d import Axes3D
ax = fig.add_subplot(111, projection='3d')
ax.scatter(normA1, normA2, normA2,c='b')

normB1 = np.random.normal(0.8,0.03,size=N1)   
normB2 = np.random.normal(0.3,0.03,size=N1) 

ax.scatter(normB1, normB2, normB2,c='r')

uniX=np.random.uniform(0,1,size=N1)
uniY=np.random.uniform(0.4,0.4,size=N1)
ax.scatter(uniX, uniY, uniY,c='k')

plt.show()