from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://www.youdao.com")

driver.find_element_by_id('border').send_keys("hello")
driver.find_element_by_id('border').submit()

time.sleep(5)

driver.quit()
