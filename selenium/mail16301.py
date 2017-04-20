from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://mail.163.com")

class Account(object):
    def __init__(self,username = " " , password = " "):
        self.username= username
        self.password= password

def do_login_as(user_info):
    driver.switch_to_frame("x-URS-iframe")
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlemail']").clear()
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlemail']").send_keys(user_info.username)
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlpwd']").clear()
    driver.find_element_by_xpath(".//*[@class='j-inputtext dlpwd']").send_keys(user_info.password)
    driver.find_element_by_xpath(".//*[@id='dologin']").click()

admin=Account(username='admin',password='123')
guest=Account(username='yulb1994',password='zxcvylb1994')

do_login_as(admin)
do_login_as(guest)

