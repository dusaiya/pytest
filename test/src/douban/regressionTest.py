# encoding: utf-8
'''
Created on 2017年7月5日

@author: alibaba
'''
import re


def isAllNum(str):
    pattern=re.compile(r"\d+$",re.I)
    match =pattern.match(str)
    if match:
        return True
    else:
        return False  

