from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# ActionChains 类提供的鼠标操作的常用方法：
#  perform() 执行所有ActionChains 中存储的行为
#  context_click() 右击
#  double_click() 双击
#  drag_and_drop() 拖动
#  move_to_element() 鼠标悬停



# driver=webdriver.Firefox()
# driver.get("http://pan.baidu.com/disk/home?errno=0&errmsg=Auth%20Login%20Sucess&&bduss=&ssnerror=0#list/path=%2F&vmode=list")
# # 定位到要右击的元素
# right_click=driver.find_element_by_id(".//*[@id='layoutMain']/div[2]/div[3]/div/div/dd[1]/div[2]/div[1]")
# # 对定位到的元素执行鼠标右键操作
# ActionChains(driver).context_click(right_click).perform()


driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

above=driver.find_element_by_class_name("pf")
ActionChains(driver).move_to_element(above).perform()
sleep(10)



