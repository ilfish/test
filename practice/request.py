import requests
from bs4 import BeautifulSoup
import os
import sys

headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url='http://www.mzitu.com/all'
start_html=requests.get(all_url,headers)
# print (start_html.text)

Soup=BeautifulSoup(start_html.text,'lxml')
# li_list=Soup.find_all('li')
# for li in li_list:
#     print(li)

all_a=Soup.find('div',class_='all').find('a')
# for a in all_a:
title=all_a.get_text()
href=all_a['href']
# print(title ,href)
html=requests.get(href,headers)
html_soup=BeautifulSoup(html.text , 'lxml')
max_span=html_soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
# print (max_span)
for page in range(1,int(max_span)+1):
    page_url=href+'/'+str(page)
    # print (page_url)
    img_html=requests.get(page_url,headers)
    img_soup=BeautifulSoup(img_html.text,'lxml')
    img_url=img_soup.find('div',class_='main-image').find('img')['src']
    name=img_url[-9:-4]
    path='d://test'
    if not os.path.isdir(path):
        os.makedirs(path)
    img=requests.get(img_url,headers)
    f=open(name+'.jpg','ab')
    f.write(img.content)
    f.close()



