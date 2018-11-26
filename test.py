import requests



class Taobaospider(object):
	"""docstring for Taobaopider"""
	def __init__(self):
		self.url = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.1d1429ebAeMgFH&id=539563860487&skuId=3839645105290&areaId=140100&user_id=1099691863&cat_id=50025174&is_b=1&rn=3fe9683f9ccba5f935e50d966ec15b1f"
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400"}
		self.offset = 1

	def start_request(self):
		print("我正在爬取第%d页..."%self.offset)
		content = requests.get(self.url,headers=self.headers).content.decode()
		print(content)

	def content_re(self,content):
		rateDate = re





if __name__ == "__main__":
	spider = Taobaospider()
	spider.start_request()
