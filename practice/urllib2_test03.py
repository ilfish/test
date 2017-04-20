# -*- coding:utf-8 -*-
# GET方法
import urllib

values={"username":"1016903103@qq.com","password":"123456"}
data=urllib.urlencode(values)

url="http://passport.csdn.net/account/login"
geturl=url+'?'+data

request=urllib.Request(geturl)
response=urllib.urlopen(request)
html=response.read()
# print html
print (geturl)
