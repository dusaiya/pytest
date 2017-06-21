# encoding: utf-8
'''
Created on 2017年6月1日

@author: alibaba
'''
import json
from douban.ApiModule import ApiModule


#name='35661509'
#content=doubanuser(name)
def doubanresult(content):
    ctob=json.loads(content)
    
    apiMd=ApiModule()
    apiMd.set_loc_id(ctob['loc_id'])
    apiMd.set_name(ctob['name'])
    apiMd.set_created(ctob['created'])
    apiMd.set_is_banned(ctob['is_banned'])
    apiMd.set_is_suicide(ctob['is_suicide'])
    apiMd.set_loc_name(ctob['loc_name'])
    apiMd.set_avatar(ctob['avatar'])
    apiMd.set_signature(ctob['signature'])
    apiMd.set_uid(ctob['uid'])
    apiMd.set_alt(ctob['alt'])
    apiMd.set_desc(ctob['desc'])
    apiMd.set_type(ctob['type'])
    apiMd.set_id(ctob['id'])
    apiMd.set_large_avatar(ctob['large_avatar'])
    return apiMd
"{\"loc_id\":\"118159\",\"name\":\"\u6b6a\u574f\u5bc6\u7801\u03b2\",\"created\":\"2010-02-21 21:09:31\",\"is_banned\":false,\"is_suicide\":false,\"loc_name\":\"\u6c5f\u82cf\u5357\u4eac\",\"avatar\":\"https://img3.doubanio.com\\/icon\\/u35661509-20.jpg\",\"signature\":\"\u8fd9\u4e2a\u8282\u594f\u548c\u6c14\u6c1b\u5f88\u719f\u6089\uff0cany way.\",\"uid\":\"35661509\",\"alt\":\"https:\\/\\/www.douban.com\\/people\\/35661509\\/\",\"desc\":\"\u5347\u5de8\u87f9\uff0c\u5c31\u8fd9\u6837\u3002\",\"type\":\"user\",\"id\":\"35661509\",\"large_avatar\":\"https://img3.doubanio.com\\/icon\\/up35661509-20.jpg\"}"
