import requests   #导包
import json
import time

#统一资源定位符  网址
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'


header = {
	'Referer':'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'	

	}

# print(jsonData)

for pn in range(1,31):
	#json数据
	dat ={
		'first':'false',
		'pn':pn,
		'kd':'Python'
	}

	#变量
	html = requests.post(url, headers=header, data=dat)

	time.sleep(1)

	#提取数据
	jsonData = html.json()
	content = jsonData['content']['positionResult']['result']

	print(content)

	items = {}

	for item in content:

		items['salary'] = item['salary']
		items['positionName'] = item['positionName']
		items['companyFullName'] = item['companyFullName']


	
	# a 代表追加
	# with open('test5.json', 'a', encoding='utf-8') as fp:

	# 	salary = json.dumps(items, ensure_ascii=False) + '\n'

	# 	fp.write(salary)