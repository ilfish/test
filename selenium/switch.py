from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
sleep(5)

search_windows=driver.current_window_handle

driver.find_element_by_class_name('lb').click()
driver.find_element_by_link_text(u'立即注册').click()

all_hands=driver.window_handles

for handle in all_hands:
    if handle!=search_windows:
        driver.switch_to_window(handle)
        print(u"现在是注册窗口！")
        driver.find_element_by_name("userName").send_keys("username")
        # sleep(5)
        driver.find_element_by_ame("password").send_keys("password")
        # sleep(5)


for  handle in all_hands:
    if handle==search_windows:
        driver.switch_to_window(handle)
        print(u"现在是搜索窗口")
        driver.find_element_by_id("TANGRAM__PSP_2__closeBtn").click()
        driver.find_element_by_id('kw').send_keys("helloworld")
        driver.find_element_by_id('su').click()
        sleep(5)
