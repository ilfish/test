from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw22").send_keys("helloworld ")
