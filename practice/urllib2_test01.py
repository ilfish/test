import urllib
response=urllib.urlopen('http://www.baidu.com/')
html=response.read()
print (html)
