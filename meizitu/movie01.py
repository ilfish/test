import requests
from bs4 import BeautifulSoup


headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
url=("https://movie.douban.com/top250?start={page}&filter=&type=")
start_html=requests.get(url, headers)
# print(start_html.text)

soup=BeautifulSoup(start_html.text, 'lxml')
all_a=soup.find('ol', class_='grid_view').find_all('a')
for a in all_a:
    print(a)

