import requests
from lxml import etree

heards={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url="http://www.mzitu.com/all"
html_start=requests.get(all_url,heards)
# print(html_start.text)

html=etree.HTML(html_start.text)
