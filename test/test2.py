import requests
import re
import time



class Taobaospider(object):
	"""docstring for Taobaopider"""
	def __init__(self):     #
		self.url = "https://item.taobao.com/item.htm?id=576964637601&ali_refid=a3_420432_1006:1123500828:N:t恤:cd7b8954c4092eabb109b99c28ae0629&ali_trackid=1_cd7b8954c4092eabb109b99c28ae0629&spm=a230r.1.14.1#detail"
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400"}
		self.offset = 1

	def start_request(self):
		print("我正在爬取第%d页..." % self.offset)
		content = requests.get(self.url,headers=self.headers).content.decode('gb18030')     #编码问题
		# time.sleep(1)
		# print(content)
		self.content_re(content)

	def content_re(self,content):
		rateDate = re.findall(r"(\w+)\s", content)
		rateContent = re.findall(r'"rateContent":"(.*?)"', content)
		auctionSku = re.findall(r'"auctionSku":"(.*?)"', content)
		print(rateContent,rateDate,auctionSku)
		for date, content ,sku in zip(rateDate,rateContent,auctionSku):
			items = {"评论时间":date, "评论内容":content, "付款方式":sku}
			i = json.dumps(items,ensure_ascii=False) + "\n"
			print(i)





if __name__ == "__main__":     #启动程序
	spider = Taobaospider()
	spider.start_request()
