from selenium import webdriver
import time

def login(driver):
    driver.switch_to_frame("x-URS-iframe")
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlemail']").clear()
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlemail']").send_keys("yulb1994")
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlpwd']").clear()
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlpwd']").send_keys("zxcvylb1994")
    driver.find_element_by_xpath(".//*[@id='dologin']").click()

def logout(driver):
    driver.find_element_by_link_text(u"退出").click()
    # driver.find_element_by_xpath("//*[@id='_mail_component_39_39']/a").click()
    # time.sleep(5)


