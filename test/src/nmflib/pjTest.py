# encoding: utf-8
'''
Created on 2016年11月15日

@author: alibaba
'''
import numpy as np
#from basenmf import BaseNMF, NMFResult
#from projective import ProjectiveNMF
from nmf import NMF

X=np.array([(1,2,3,4,5,6),(4,5,6,7,8,9),(1,3,5,4,2,6)])/10.0
nmf=NMF(X,2,maxiter=100)
nmf_result=nmf.predict()
w_nmf = nmf_result.matrices[0]
print(w_nmf)
