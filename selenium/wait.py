from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions
# 用as关键字对expected_conditions类重命名为EC
# from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

element=WebDriverWait(driver,5,0.5).until(expected_conditions.presence_of_element_located((By.ID,'kw')))
# element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'kw')))

element.send_keys('selenium')

# driver.quit()
