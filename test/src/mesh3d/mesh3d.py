# encoding: utf-8
'''
Created on 2016年12月27日

@author: alibaba
'''
import numpy as np
import matplotlib.pyplot as plt



N1=300
normA1 = np.random.normal(0.2,0.03,size=N1)   
normA2 = np.random.normal(0.5,0.03,size=N1) 

normB1 = np.random.normal(0.8,0.03,size=N1)   
normB2 = np.random.normal(0.3,0.03,size=N1) 


uniX=np.random.uniform(0,1,size=N1)
uniY=np.random.uniform(0.4,0.4,size=N1)

plt.plot(normA1,normA2,'r+')
plt.plot(normB1,normB2,'b*')
plt.plot(uniX,uniY,'ko')

plt.show()