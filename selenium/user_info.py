from selenium import webdriver
import time

user_file=open('user_info.txt','r')
values=user_file.readlines()
user_file.close()

for serch in values:
    username=serch.split(',')[0]
    # print(username)
    password=serch.split(',')[1]
    # print(password)
    driver=webdriver.Chrome()
    driver.set_window_position(720,0)
    driver.get("http://mail.163.com")
    driver.switch_to_frame("x-URS-iframe")
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlemail']").clear()
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlemail']").send_keys(username)
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlpwd']").clear()
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlpwd']").send_keys(password)
    driver.find_element_by_xpath(".//*[@id='dologin']").click()
    time.sleep(5)
    driver.quit()
