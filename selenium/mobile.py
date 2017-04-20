from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://m.mail.10086.cn")

# print(u"设置浏览器宽480、高800显示")
# driver.set_window_size(480,800)

print(u"全屏幕显示")
driver.maximize_window()

# driver.quit()
