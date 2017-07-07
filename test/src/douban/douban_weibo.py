# encoding: utf-8
'''
Created on 2017年7月3日

@author: alibaba
'''

import re
import json

def line2str(line):
    """Deserialize
    将行内容转换成字符串
    """
    ulink = json.loads(line)
    keys = ulink.keys()
    values = ulink[keys[0]]
    val_lens = len(values)
    strValues=[None]*val_lens
    for j in range(0, val_lens):
        print values[j].__str__()
        strValues[j]=values[j].__str__()
    return keys[0].__str__(),strValues

def isAllNum(str):
    pattern=re.compile(r"\d+$",re.I)
    match =pattern.match(str)
    if match:
        return True
    else:
        return False  


