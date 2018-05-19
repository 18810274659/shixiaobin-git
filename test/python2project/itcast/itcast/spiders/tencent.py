# -*- coding: utf-8 -*-
import scrapy
from itcast.tencentItems import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['http://hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    
    def parse(self, response):
	node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
	for node in node_list:
#		print  node.xpath["./td[1]/a/text()"].extract()[0]

		item =  TencentItem()
		item['position'] = node.xpath("./td[1]/a/text()").extract()[0].encode('utf-8')
		print '----------------------------' 
		#print tencent['position'] + '----------------------------------------------------------'
		yield item	
