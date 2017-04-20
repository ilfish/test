from selenium import webdriver
import time

file_info=open('info.txt','r')
values=file_info.readlines()
file_info.close()

for serch in values:
    driver=webdriver.Chrome()
    driver.set_window_position(720,0)
    driver.get("http://www.baidu.com")
    print("search "+serch)
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys(serch)
    driver.find_element_by_xpath('//*[@id="su"]').click()
    time.sleep(5)
    driver.quit()
