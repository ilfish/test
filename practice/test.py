import requests
import os
from bs4 import BeautifulSoup

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.1(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
Surl = 'http://www.mzitu.com/all'
r = requests.get(Surl,headers=headers)
Soup = BeautifulSoup(r.text,'lxml')
all_a = Soup.find('div',class_='all').find_all('a')
for a in all_a:
    title = a.get_text()
    href = a['href']
    #print(title,href)
    r2 = requests.get(href,headers=headers)
    r2_Soup = BeautifulSoup(r2.text,'lxml')
    max_span = r2_Soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1, int(max_span) + 1):
        page_url = href + '/' + str(page)
        r3 = requests.get(page_url,'lxml')
        r3_Soup = BeautifulSoup(r3.text,'lxml')
        img_url = r3_Soup.find('div',class_='main-image').find('img')['src']
       # print(img_url)
        name = img_url[-9:-4]
        root = "D://mzitu//"
        path = root + name
        try:
            if not os.path.exists(root):
                os.mkdir(root)
                print("File make success")
            if not os.path.exists(path):
               image = requests.get(img_url, headers=headers)
               with open(name+'.jpg', 'ab') as f:
                    f.write(image.content)
                    f.close()
                    print("保存文件成功")
            else:
                print("文件YI存在")
        except:
            print("faild")
