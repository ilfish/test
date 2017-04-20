from selenium import webdriver
import mpublic163
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
# driver.get_window_position(720,0)
driver.get("http://mail.163.com")

mpublic163.login(driver)
time.sleep(5)

mpublic163.logout(driver)
time.sleep(5)

driver.quit()
