import requests
import re
import time
import json
import xlwt


class getData2(object):
	#初始化函数
	def __init__(self):     #初始化数据为书籍销量相关信息
		self.url='http://book.kongfz.com/widget/ajax?widget=shopInfo&tpl=store&api=get90DayAverage&&shopId=241045&userId=7559598&_=1543383981457'   #销量网址
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'}


	def start_request(self):
		bookName = self.getBookName()   #获取书店名称
		# print(bookName[0])
		orderCount = self.getSaleNum()    #获取销量
		content = self.getComment()       #获取评价
		aa = json.loads(content[0])     #json.loads(): 对数据进行解码。	
		print(aa)
		print(aa['result']['reviewList'][0]['appraisedNickname'])     #书店名称
		print(aa['result']['reviewList'][0]['content'])    #书店评价
		print(aa['result']['reviewList'][0]['buyerLevel']['star'])    #书店评价（小星星）
		# print("******")
		 


		book = xlwt.Workbook(encoding='utf-8')     # 创建一个excel对象
		sheet = book.add_sheet('Sheet1',cell_overwrite_ok=True) # 添加一个sheet页
		headData = ['书店','销量','评价','书店评价(星星书目)']
		for i in range(len(headData)):   #0123
			sheet.write(0,i,headData[i])   #0开始， i为列   headData[i]为数据			
		book.save('北京华鑫国盛图书有限公司2.xls')    #保存




		index =1   #行数
		for item in content:
			item = json.loads(item)
			# print(item['result']['reviewList'])
			sheet.write(index,0,bookName)    #将书店名称写入
			sheet.write(index,1,orderCount)    #将销量写入
			book.save('北京华鑫国盛图书有限公司2.xls')
			
			
		index2 = 0   #当前数组的索引
		index3 = 1   #行数
		current = []
		for item in content:
			item = json.loads(item)
			# print(item['result']['reviewList'][0])
			print(len(item['result']['reviewList'])) 
			current.append(item)
			for i in range(len(item['result']['reviewList'])):
				# print(current[index2]['result']['reviewList'][i]['buyerLevel']['star'])
				# print(current[index2]['result']['reviewList'][i]['buyerLevel']['diamond'])
				sheet.write(index3,2,current[index2]['result']['reviewList'][i]['content']);
				num = current[index2]['result']['reviewList'][i]['buyerLevel']['star'] + current[index2]['result']['reviewList'][i]['buyerLevel']['diamond']
				# print(num)
				sheet.write(index3,3,num)    #s.strip()删除左右两边的空格
				index3+=1
			index2+=1
			book.save('北京华鑫国盛图书有限公司2.xls')


	#获取书店名称
	def getBookName(self):    
		url = 'http://book.kongfz.com/241045/1015261600/'
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'}
		content = requests.get(url, headers=headers).content.decode()   #爬取的源代码
		#正则匹配获取书店名称
		reg = re.compile(r' <meta property="og:product:nick" content="name=(.*?); url=',re.S)
		bookName = re.findall(reg,content)
		# print(item)
		return bookName


	#获取书籍销售量
	def getSaleNum(self):     
		content = requests.get(self.url, headers=self.headers).content.decode()
		# print(content)
		item = json.loads(content)    #转化为json数据格式
		orderCount = item['result']['orderCount']
		# print(orderCount)
		return orderCount
		

	#获取评价并返回评价分页的数组
	def getComment(self):    
		print("我正在爬取数据...")
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'}
		time.sleep(1)
		content = []
		index = 0
		for i in range(1,8):
			url = "http://book.kongfz.com/Pc/Ajax/getShopReviewList?userId=7559598&itemId=&page=%d&needEmpty=0&rating=all" % i     #进行分页
			# print(url)
			lists = requests.get(url, headers=headers).content.decode()
			# print(lists)
			content.append(lists)    #append() 方法用于在列表末尾添加新的对象。
			# content[index] = requests.get(url, headers=headers).content.decode()      #越界https://blog.csdn.net/Norsaa/article/details/77674193
			# print(content[index])
			# print(index)
			index+=1	
		print(len(content))
		return content

		

if __name__ == '__main__':
	getD = getData2()
	getD.start_request()
	# getD.getSaleNum()
	# getD.bookName()
