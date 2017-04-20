# -*- coding:utf-8 -*-
import urllib

url='http://passport.csdn.net/account/login'
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values={'uesrname':'123456789@qq.com','password':'123456'}
headers={'Uesr-Agent':user_agent}

data=urllib.urlencode(values)

request=urllib.Request(url,data,headers)
response=urllib.urlopen(request)
html=response.read()
print (html)

