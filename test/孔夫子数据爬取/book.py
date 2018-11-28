import requests
import re
import time
import json
import xlwt


class GetData(object):
	"""docstring for GetData"""
	def __init__(self):
		# self.url = "http://item.kongfz.com/book/48444669_0_0_" + i + ".html"    #字符串的连接
		# self.url = "http://item.kongfz.com/book/48444669_0_0_1.html"    #字符串的连接
		self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'}
		self.offset = 1

	def start_request(self):
		time.sleep(1)
		content = self.get()
		# reg = re.compile(r'class="con-press-title gray6"><a href="(.*?)".*?</a>',re.S)
		reg = re.compile(r'<div class="list-con-product gray3.*?">(.*?)</div>.*?class="con-press-title gray6">.*?>.*?(.*?)</a>.*?<div class="con-press-city gray9">(.*?)</div>.*?<span style="font-weight: bold;">(.*?)</span>',re.S)
		items = re.findall(reg,content)
		# item = items.
		print(len(items))
		jsonData = json.dumps(items[0])
		return items
		

		
	def get(self):     #获取源代码
		print("我正在爬取第%d页..." % self.offset)

		content = ""
		for i in range(1,3):
			url = "http://item.kongfz.com/book/48444669_0_0_%d.html" % i     #进行分页
			content += requests.get(url, headers=self.headers).content.decode()
		# print(content)
		return content
	
	def excel_write(self,items):     #创建表
		book = xlwt.Workbook(encoding='utf-8')     # 创建一个excel对象
		sheet = book.add_sheet('Sheet1',cell_overwrite_ok=True) # 添加一个sheet页
		headData = ['品相','书店','地址','价格']
		for i in range(len(headData)):   #0123
			sheet.write(0,i,headData[i])   #0开始， i为列   headData[i]为数据
			
		book.save('book.xls')    #保存
		
		index = 1
		for  item in items:
			print(item)
			#book = json.dumps(item)
			#print(book)
			for i in range(len(headData)):
				# print(item[i])
				# a = json.dumps(item)
				# print(a)
				sheet.write(index,i,item[i].strip())    #s.strip()删除字符左右的空格
			index+=1
			book.save('book.xls')

			


if __name__ == "__main__":   #文件入口
	getD = GetData()
	items = getD.start_request()
	#print(items)
	getD.excel_write(items)
	