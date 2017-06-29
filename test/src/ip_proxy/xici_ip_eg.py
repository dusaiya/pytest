# -*- coding: utf-8 -*-
'''
Created on 2017年6月12日
从国内高匿代理IP网站中获取动态ip信息
@see:  http://www.xicidaili.com/nn/1
@author: dzm
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import scrapy
from pyquery import PyQuery as pq

class IpXicidailiSpider(scrapy.Spider):
    name="ip_xicidaili"
    allowed_domains = ["xicidaili.com"]
    start_urls = [
        "http://www.xicidaili.com/nn"
    ]

    def parse(self, response):
        print(response.url)
        # 请求第一页
        yield scrapy.Request(response.url+'/1', callback=self.parse_item, dont_filter=True)
        # 请求其他页
        soup = pq(response.body)
        pageSum = soup('.pagination a:nth-last-child(2)').text()
        print('pageSum is %s ', pageSum);
        if pageSum:
            for i in range(2, int(pageSum)):
                url = response.url+ '/' + str(i)
                yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self,response):
        print('现在开始爬取的网址是  %s' , response.url);
        soup = pq(response.body)
        trs = soup('#ip_list tr')
        if trs:
            for i in range(2, trs.length):
                tr = trs.eq(i)
                if tr:
                    # 超过3s代理，以及存货时间为小时、分的过滤掉
                    life = tr('td:eq(8)').text()
                    if self.is_valid_time(life=life):
                        speed = tr('td:eq(6) > div').attr('title')
                        speed = self.filter_speed(speed);
                        if speed < 3:
                            # 速度超过3s的代理视为太慢，不考虑
                            print tr('td').eq(1).text()
                            print tr('td').eq(2).text()
                            print tr('td').eq(5).text()
                            print self.filter_life(life)
                            print speed


    def filter_speed(self,speed):
        speed = speed.replace(u'秒','')
        return float(speed)

    def filter_life(self,life):
        '''
                        过滤存活时间
        '''
        life = life.replace(u'天','')
        return life

    def is_valid_time(self,life):
        '''
                        判断是否是有效的时间
        '''
        if life.rfind(u'分')>=0 or life.rfind(u'时')>=0:
            return False
        else:
            return True   
