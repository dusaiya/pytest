# encoding: utf-8
'''
Created on 2017年7月3日
@author: alibaba
'''

import re
import json

def line2str(line):
    """Deserialize
    将豆瓣抓去的【sina uid/】内容，按行转换成字符串
    """
    ulink = json.loads(line)
    keys = ulink.keys()
    values = ulink[keys[0]]
    val_lens = len(values)
    strValues=[None]*val_lens
    for j in range(0, val_lens):
        strValues[j]=values[j].__str__()
    return keys[0].__str__(),strValues

def doubanInfo2dict(userId,weiboIds):
    data = {"doubanId":userId, "weiboIds":""}
    weiboList = []
    for weiboId in weiboIds:
        weiboLine={"weiboId":weiboId}
        weiboList.append(weiboLine)
    data[weiboIds]=weiboList
    
def isAllNum(areastr):
    pattern=re.compile(r"\d+$",re.I)
    match =pattern.match(areastr)
    if match:
        return True
    else:
        return False  


