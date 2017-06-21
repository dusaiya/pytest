# encoding: utf-8
'''
Created on 2016年11月23日

@author: alibaba
'''
import numpy as np
from matplotlib import pyplot

def loadMatrix():
    matrix=[[10.2352,11.3220],
            [10.1223,11.8110],
            [9.1902,8.9049],
            [9.3064,9.8474],
            [8.3301,8.3404],
            [10.1528,10.1235],
            [10.4085,10.8220],
            [9.0036,10.0392],
            [9.5349,10.0970],
            [9.4982,10.8254]
            ]
    return matrix



if __name__ == "__main__":
    matA=loadMatrix()
    matC=np.array(matA)
    meanA=np.mean(matA,axis=0)
    matB=matA-meanA
    covB=np.cov(matB.T)
    eigB,eigVecB=np.linalg.eig(covB)
    sortEigB=np.argsort(eigB)
    k=1
    size=np.size(sortEigB)
    resultV=eigVecB[:,size-k:size]
    
#     print covB
#     print eigB
#     print eigVecB
#     print matB
#     print resultV
    
    resultPoint= (np.dot(matB,resultV)+np.mean(meanA)).T
    resultPoint=np.sort(resultPoint)
    print resultPoint
    arA=np.array(matA)
    pyplot.plot(arA[:,0],arA[:,1],marker='o',linestyle='None')
    pyplot.plot(resultPoint[0],resultPoint[0])
    
    pyplot.show()
      
     