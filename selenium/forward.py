from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

first_url="http://www.baidu.com"
print(u"现在访问第一个页面：{}".format(first_url))
driver.get(first_url)

second_url="http://news.baidu.com"
print(u"现在访问第二个页面：{}".format(second_url))
driver.get(second_url)

print("5秒后返回至:{},".format(first_url))
for t in range(1,6):
    print(6-t)
    sleep(1)
driver.back()

print("现在前进至:{},".format(second_url))
driver.forward()

# driver.quit()
