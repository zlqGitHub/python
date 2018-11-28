import requests
import time

class Taobaospider(object):
	"""docstring for Taobaospider"""
	def __init__(self):
		self.url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
		self.headers = {
			'Referer':'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400"
			}
		self.offset = 1


	def start_request(self):
		print("我正在爬取第%d页..." % self.offset)
		time.sleep(1)
		dat = {
			'first':'false',
			'pn':1,
			'kd':'Python'
		}
		# content = requests.get(self.url, headers=self.headers).content.decode()
		content = requests.post(self.url, headers=self.headers, data=dat)
		jsonData = content.json()['content']['positionResult']['result']
	
		print(jsonData)



if __name__=="__main__":
	spider = Taobaospider()
	spider.start_request()