import urllib.request
import urllib.parse
import random
import re
import string
from bs4 import BeautifulSoup

url = 'http://opac.snnu.edu.cn:8991/F'

iplist = ['221.228.17.172' , '101.236.22.141' , '115.46.75.94' , '114.229.125.223' , '101.236.60.8']

proxy_support = urllib.request.ProxyHandler({'https':random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

soup = BeautifulSoup(html , 'lxml')

p = soup.find('a' , attrs={"title": "预约到馆"})
urlx = p.get('href')

reqs = urllib.request.Request(urlx)
reqs.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')

response = urllib.request.urlopen(reqs)
html = response.read().decode('utf-8')

soup = BeautifulSoup(html , 'lxml')

data = {}
DATA = []
lt = ['预约者' , '书名' , '著者' , '保留结束日期' , '单侧分馆' , '取书地点']
number = 0

for i in soup.find_all('td'):
    number += 1
    j = str(i.text)
    if number > 4:
        j = j.strip()
        j = j.replace('\n' , '')
        data[lt[(number - 4) % 6]] = j
        if number - 4 != 0 and (number - 4) % 6 == 0:
            DATA.append(data.copy())
            data.clear()



