from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://mail.163.com")

driver.switch_to_frame('x-URS-iframe')

driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("yulb1994")


# driver.find_element_by_xpath(".//input[@name='email']").clear()
# driver.find_element_by_xpath(".//input[@class='j-inputtext dlemail' and @name='email']").send_keys("hello")

driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("zxcvylb1994")

driver.find_element_by_id("dologin").click()

# driver.quit()

# driver=webdriver.Firefox()
# driver.get("http://www.126.com")
# driver.find_element_by_id("idInput").clear()
# driver.find_element_by_id("idInput").send_keys("username")
# driver.find_element_by_id("pwdInput").clear()
# driver.find_element_by_id("pwdInput").send_keys("pawdword")

# driver.find_element_by_id("loginBtn").click()
