import requests
from bs4 import BeautifulSoup
import os
# import re

class movice():

    def request(self,url):
        headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        html=requests.get(url,headers)
        return html



Movice = movice()
Movice.url=("https://movie.douban.com/top250?start={page}&filter=&type=")
