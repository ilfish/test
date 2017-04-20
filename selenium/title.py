from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.126.com")

print("before login==========")

title=driver.title
print(title)

now_url=driver.current_url
print(now_url)



driver.quit()
