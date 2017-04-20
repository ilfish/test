# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time


# logging.basicConfig(level=logging.DEBUG)
driver =webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()

# driver.find_element_by_xpath(".//*[@id='kw']").send_keys("helloworld")
# driver.find_element_by_xpath(".//*[@id='su']").click()

# driver.find_element(By.ID,"kw").send_keys("Python")
# driver.find_element(By.ID,"su").submit()

time.sleep(5)

driver.quit()


