#encoding:utf-8

from bs4 import BeautifulSoup
import  requests
import lxml

#做网络请求
#requests

#分析网页
#bs4

#把数据抓过来(requstes)


headeas = {

'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Mobile Safari/537.36',


'Upgrade-Insecure-Requests':'1',
'Host':'www.weather.com.cn',
'Referer':'http://www.weather.com.cn/textFC/db.shtml'
}



html = requests.get('http://www.weather.com.cn/textFC/hb.shtml',headers = headeas)
content =  html.content

soup = BeautifulSoup(content,'lxml')
conMid_list = soup.find('div',class_='conMidtab')

conMid2_list = soup.find_all('div',class_='conMidtab2')

for x in conMid2_list:
    tr_list = x.find_all('tr')
    province = tr_list[2]
    print province.text


