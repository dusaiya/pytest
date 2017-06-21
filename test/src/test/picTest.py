# encoding: utf-8
'''
Created on 2016年11月10日

@author: alibaba
'''
import numpy as np
import matplotlib.pyplot as plt


t = np.arange(0., 5., 0.2)
line,=plt.plot([1,2,3,4])
line.set_antialiased(False)
plt.ylabel('some numbers')
plt.show()
# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()
'''

H=np.array([(1,0,0),(0,0,1)])
W=np.array([(2,3),(4,5),(6,7)])
#print(H)
#print(H.T)
print()
'''
