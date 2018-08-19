import urllib.request
import urllib.parse
import random
import re
from bs4 import BeautifulSoup

x = input('请输入您的校园卡账号：')
x = int(x)
data = {}
data['usernum'] = x
data['search'] = '查询'
data['wx'] = ''

data = urllib.parse.urlencode(data).encode('utf-8')

url = 'http://edutech.snnu.edu.cn/ecard/ccc.asp'

iplist = ['221.228.17.172' , '101.236.22.141' , '115.46.75.94' , '114.229.125.223' , '101.236.60.8']

proxy_support = urllib.request.ProxyHandler({'https':random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

req = urllib.request.Request(url , data)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

soup = BeautifulSoup(html , 'lxml')

key = ['卡号' , '时间' , '次数' , '原金额' , '交易额' ,'卡余额' , '记录信息' , '备注']
DATA = []
mp = {}
num = 0

for i in soup.find_all('td'):
    mp[key[num % 8]] = i.string
    if(num % 8 == 0 and num != 0):
        DATA.append(mp.copy())
        mp.clear()
    num = num + 1
    



