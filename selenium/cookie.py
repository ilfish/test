from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.youdao.com")

# #获取 cookie 信息
# cookie=driver.get_cookies()
# #将获得的 cookie 信息打印
# print(cookie)


#向 cookie 中的 name 和 value 添加会话信息
driver.add_cookie({'name':'key-aaaaaa','value':'value-bbbbbb'})

#遍历cookies 中的name 和value 信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s"%(cookie['name'],cookie['value']))

driver.quit()
