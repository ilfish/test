# -*- coding:utf-8 -*-
import re
import requests

iplist=[]   #初始化list列表存放获取到额ip
html=requests.get("http://haoip.cc/tiqu.htm")
iplistn=re.findall(r'r/>(.*?)<b',html.text,re.S) #从html.text中获取所有r/><b中的内容;re.s：包括匹配换行符;finall返回的是一个list
for ip in iplistn:
    i=re.sub('\n','',ip)      #re.sub将\n替换为空
    iplist.append(i.strip())  #i.strip():去掉字符串的空格
    print(i.strip())
# print(iplist)
