from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://github.com")

elem = driver.find_element(By.NAME, "Where")
elem.clear()
elem.send_keys("Where")
elem.send_keys(Keys.RETURN)
print(elem)
