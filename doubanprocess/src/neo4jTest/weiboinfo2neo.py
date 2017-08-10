# encoding: utf-8
'''
Created on 2017年8月4日

@author: alibaba

'''   
##{name: {name}, title: {title}}.

from neo4j.v1 import GraphDatabase,basic_auth
##必须按照如下写，即使是在 10.200.6.5 这台机器上
driver = GraphDatabase.driver("bolt://10.200.6.5:7687", auth=basic_auth("neo4j", "ictsoftware"))
neo_session = driver.session()

from pymongo import MongoClient
conn=MongoClient("10.200.6.7",27017)
douban_db=conn.douban_weibo


def insertWeiboInfo(neo_session, result):
    print result
    print result.__class__
    newDict = {}
    for key in result.keys():
        keystr = key.__str__()
        print keystr
        weiboValue = result[keystr]
        print weiboValue.__class__
        if type(weiboValue) is unicode:
            newDict[keystr] = weiboValue.encode('utf-8')
        elif type(weiboValue) is int:
            newDict[keystr] = weiboValue
        else:
            newDict[keystr] = weiboValue.__str__()
    neo_session.run("CREATE (:weibo_person {bi_followers_count:{bi_followers_count}, " + "domain:{domain}, avatar_large:{avatar_large}, verified_source:{verified_source}," + "ptype:{ptype}, block_word:{block_word}, statuses_count:{statuses_count}, " + "id:{id}, verified_reason_url:{verified_reason_url}, " + "city:{city}, verified:{verified}, credit_score:{credit_score}, insecurity:{insecurity}, block_app:{block_app}, follow_me:{follow_me}, verified_reason:{verified_reason}, followers_count:{followers_count}, location:{location}, verified_trade:{verified_trade}, mbtype:{mbtype}, verified_source_url:{verified_source_url}, profile_url:{profile_url}, status:{status}, avatar_hd:{avatar_hd}, star:{star}, description:{description}, friends_count:{friends_count}, online_status:{online_status}, mbrank:{mbrank}, idstr:{idstr}, profile_image_url:{profile_image_url}, allow_all_act_msg:{allow_all_act_msg}, allow_all_comment:{allow_all_comment}, geo_enabled:{geo_enabled}, class:{class}, screen_name:{screen_name}, lang:{lang}, weihao:{weihao}, remark:{remark}, favourites_count:{favourites_count}, name:{name}, url:{url}, province:{province}, created_at:{created_at}, user_ability:{user_ability}, story_read_state:{story_read_state}, verified_type:{verified_type}, gender:{gender}, following:{following}, pagefriends_count:{pagefriends_count}, urank:{urank}, _id:{_id}})", newDict)
 
results=list(douban_db.weibo_info.find())
for resultboOb in results:
#result = results[0]
    insertWeiboInfo(neo_session, resultboOb)
neo_session.close()

# 
#neo_session.run("CREATE (a:Person {name: {name}, title: {title}})",
#           {"name": "Arthur", "title": "King"})
# 
# result = neo_session.run("MATCH (a:Person) WHERE a.name = {name} "
#                     "RETURN a.name AS name, a.title AS title",
#                     {"name": "Arthur"})
#for record in result:
#   print("%s %s" % (record["title"], record["name"]))
conn.close()



