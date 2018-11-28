import requests
import re
import time
import json
import xlwt


class getData2(object):
	"""docstring for Taobaospi"""
	def __init__(self):     #初始化数据为书籍销量相关信息
		self.url='http://book.kongfz.com/widget/ajax?widget=shopInfo&tpl=store&api=get90DayAverage&&shopId=171476&userId=4321758&_=1543386920623'   #销量网址
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'}



	def start_request(self):
		bookName = self.getBookName()   #获取书店名称
		print(bookName[0])
		orderCount = self.getSaleNum()    #获取销量
		content = self.getComment()
		aa = json.loads(content[0])     #json.loads(): 对数据进行解码。	
		print(aa['result']['reviewList'][0]['appraisedNickname'])     #书店名称
		print(aa['result']['reviewList'][0]['buyerLevel']['star'])    #书店评价（小星星）
		# print("******")
		 


		book = xlwt.Workbook(encoding='utf-8')     # 创建一个excel对象
		sheet = book.add_sheet('Sheet1',cell_overwrite_ok=True) # 添加一个sheet页
		headData = ['书店','销量','书店评价(星星书目)']
		for i in range(len(headData)):   #012
			sheet.write(0,i,headData[i])   #0开始， i为列   headData[i]为数据			
		book.save('书海之心.xls')    #保存




		index =1
		for item in content:
			item = json.loads(item)
			# print(item['result']['reviewList'])
			sheet.write(index,0,bookName)    #将书店名称写入
			sheet.write(index,1,orderCount)    #将销量写入
			book.save('书海之心.xls')
			
			
		index2 = 0
		index3 = 1
		current = []
		for item in content:
			item = json.loads(item)
			# print(item['result']['reviewList'][0])
			# print(len(item['result']['reviewList'])) 
			current.append(item)
			for i in range(len(item['result']['reviewList'])):
				# print(current[index2]['result']['reviewList'][i]['buyerLevel']['star'])
				# print(current[index2]['result']['reviewList'][i]['buyerLevel']['diamond'])
				num = current[index2]['result']['reviewList'][i]['buyerLevel']['star'] + current[index2]['result']['reviewList'][i]['buyerLevel']['diamond']
				print(num)
				sheet.write(index3,2,num)    #s.strip()删除左右两边的空格
				index3+=1
			index2+=1
			book.save('书海之心.xls')


	def getBookName(self):    #获取书店名称
		url = 'http://book.kongfz.com/171476/1040595356/'
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'}
		content = requests.get(url, headers=headers).content.decode()
		#正则匹配获取书店名称
		reg = re.compile(r' <meta property="og:product:nick" content="name=(.*?); url=',re.S)
		bookName = re.findall(reg,content)
		# print(bookName)
		return bookName


	def getSaleNum(self):     #获取书籍销售量
		content = requests.get(self.url, headers=self.headers).content.decode()
		# print(content)
		item = json.loads(content) 
		orderCount = item['result']['orderCount']
		# print(orderCount)
		return orderCount
		

	def getComment(self):    #获取评价并返回评价分页的数组
		print("我正在爬取数据...")
		#content = []    #定义一个空数组存放值
		# url = 'http://book.kongfz.com/Pc/Ajax/getShopReviewList?userId=7559598&itemId=&page=3&needEmpty=0&rating=all'
		headers = {'User-Agent':'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'}
		time.sleep(1)
		content = []
		index = 0
		for i in range(1,21):
			url = "http://book.kongfz.com/Pc/Ajax/getShopReviewList?userId=4321758&itemId=&page=%d&needEmpty=0&rating=all" % i     #进行分页
			# print(url)
			lists = requests.get(url, headers=headers).content.decode()
			content.append(lists)
			# content[index] = requests.get(url, headers=headers).content.decode()      #越界https://blog.csdn.net/Norsaa/article/details/77674193
			# print(content[index])
			# print(index)
			index+=1	
		return content

		



if __name__ == '__main__':
	getD = getData2()
	getD.start_request()
	# getD.getSaleNum()
	# getD.getBookName()
