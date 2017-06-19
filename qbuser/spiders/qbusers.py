#_*_ coding:utf-8 _*_
import scrapy
from qbuser.items import QbuserItem
class QbuserSpider(scrapy.Spider):
	pages=100
	name='userspider'
	allowed_domains=["qiushibaike.com"]
	start_urls=["https://www.qiushibaike.com/users/33630274/followers/"]

	def parse(self,response):
		item=QbuserItem()
		h2=response.xpath('//div[@class="user-header-cover"]/h2')
		if h2:
			item['name']=h2.xpath('./text()').extract()
		ubul=response.xpath('//div[@class="user-statis user-block"][2]/ul')
		li4=ubul.xpath('./li[4]')
		if li4:
			item['homeTown']=li4.xpath('./text()').extract()
		li5=ubul.xpath('./li[5]')
		if li5:
			item['age']=li5.xpath('./text()').extract()

		yield item

		for userurl in response.xpath('//div[@class="user-block user-follow"]/ul/li/a[1]/@href').extract():
			userurl='https://www.qiushibaike.com'+userurl+'followers/'
			yield scrapy.Request(userurl,callback=self.parse)
