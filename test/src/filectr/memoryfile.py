# encoding: utf-8
'''
Created on 2017年3月28日

memory-mapped-file array
不用读取整个文件，而只处理文件中的一小部分
参数说明
##np.memmap("tmp.dat", dtype=np.int64,mode="r+",offset=0,order="C",shape=(2,5))

@author: alibaba
'''
import numpy as np

bmp=np.memmap("tmp.bmp", offset=54, shape=(1000,1000,3))

tmp=np.linspace(0,255,1000).astype(np.uint8)
bmp[:,:,0]=tmp
bmp[:,:,1]=tmp.reshape(-1,1)
bmp[:,:,2]=127
bmp.flush()