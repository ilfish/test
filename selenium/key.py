from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 在使用键盘按键方法前需要先导入keys 类包。
# 下面经常使用到的键盘操作：
# send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
# send_keys(Keys.SPACE) 空格键(Space)
# send_keys(Keys.TAB) 制表键(Tab)
# send_keys(Keys.ESCAPE) 回退键（Esc）
# send_keys(Keys.ENTER) 回车键（Enter）
# send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
# send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
# send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
# send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
# send_keys(Keys.F1) 键盘F1
# ……
# send_keys(Keys.F12) 键盘F12

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("seleniumm")
sleep(3)

# 删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
sleep(3)

# 输入空格+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
sleep(3)

# Ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
sleep(3)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
sleep(3)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
sleep(3)

# 回车代替点击操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
