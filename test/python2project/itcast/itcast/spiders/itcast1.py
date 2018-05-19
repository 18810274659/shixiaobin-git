# -*- coding: utf-8 -*-
import scrapy
#引入容器
from itcast.items import ItcastItem

class MySpider(scrapy.Spider):
    #设置name
    name = "itcast1"
    #设定域名
    allowed_domains = ["http://www.itcast.cn"]
    #填写爬取地址
    start_urls = ["http://www.itcast.cn//channel/teacher.shtml"]
    #编写爬取方法
    def parse(self, response):
	node_list = response.xpath("//div[@class='li_txt']")
	
	for node in node_list:
		item = ItcastItem()
		name = node.xpath("./h3/text()").extract()
		title = node.xpath("./h4/text()").extract()
		info = node.xpath("./p/text()").extract()
		item['name'] = name[0]
		item['title'] = title[0]
		item['info'] = info[0]
		print name[0]
		yield item

#	print response.body
        #实例一个容器保存爬取的信息
      #  item = ItcastItem()
        #这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        #先获取每个课程的div
       # for box in response.xpath('//div[@class="moco-course-wrap"]/a[@target="_self"]'):
            #获取每个div中的课程路径
        #    item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            #获取div中的课程标题
         #   item['title'] = box.xpath('.//img/@alt').extract()[0].strip()
            #获取div中的标题图片地址
          #  item['image_url'] = box.xpath('.//@src').extract()[0]
            #获取div中的学生人数
           # item['student'] = box.xpath('.//span/text()').extract()[0].strip()[:-3]
            #获取div中的课程简介
        #    item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            #返回信息
         #   yield item
	#name = 'itcast1'
	
