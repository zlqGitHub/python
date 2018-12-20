import requests
import re
import time
import json
import xlwt


class GetData(object):
	#初始化函数
	def __init__(self): 
		# self.url = "http://item.kongfz.com/book/48444669_0_0_" + i + ".html"    #字符串的连接
		# self.url = "http://item.kongfz.com/book/48444669_0_0_1.html"    #字符串的连接
		self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'}
		self.offset = 1   #页码


	def start_request(self):
		time.sleep(1)   #函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间
		content = self.get()
		# 通过正则匹配需要的数据
		reg = re.compile(r'<div class="list-con-product gray3.*?">(.*?)</div>.*?class="con-press-title gray6">.*?>.*?(.*?)</a>.*?<div class="con-press-city gray9">(.*?)</div>.*?<span style="font-weight: bold;">(.*?)</span>',re.S)
		items = re.findall(reg,content)
		# print(len(items))   测试总共有多少条数据
		#jsonData = json.dumps(items[0])   #json.dumps:将 Python 对象编码成 JSON 字符串
		return items
		

	#获取源代码	
	def get(self):    
		content = ""    #保存爬取的源代码
		for i in range(1,3):   #两页
			print("我正在爬取第%d页..." % i)
			url = "http://item.kongfz.com/book/48444669_0_0_%d.html" % i     #进行分页
			content += requests.get(url, headers=self.headers).content.decode()  #获取网页源代码
		# print(content)
		return content
	
	#创建表并将数据写入表中
	def excel_write(self,items):    
		book = xlwt.Workbook(encoding='utf-8')     # 创建一个excel对象
		sheet = book.add_sheet('Sheet1',cell_overwrite_ok=True) # 添加一个sheet页
		headData = ['品相','书店','地址','价格']
		for i in range(len(headData)):   #0123  将表格头部属性写入表中
			sheet.write(0,i,headData[i])   #0行 i为列   headData[i]为数据
			
		book.save('book2.xls')    #保存
		
		index = 1  #页数
		for item in items:
			print(item)
			#book = json.dumps(item)
			#print(book)
			for i in range(len(headData)):
				sheet.write(index,i,item[i].strip())    #s.strip()删除字符左右的空格
			index+=1
			book.save('book2.xls')

		

if __name__ == "__main__":   #文件入口
	getD = GetData()
	items = getD.start_request()
	#print(items)
	getD.excel_write(items)
	