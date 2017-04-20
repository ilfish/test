# -*- coding:utf-8 -*-
# post方法
import urllib

values={"username":"1016903103@qq.com","password":"123456"}
data=urllib.urlencode(values)
url="https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"

request=urllib.Request(url,data)
response=urllib.urlopen(request)
html=response.read()
print (html)


