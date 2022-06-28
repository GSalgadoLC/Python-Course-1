# Seleniumm
# Login to git and make sure avatar shows ur username correctly

# pip install selenium
# need a driver, pypi.org

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("ninjacoder22")
password_box = browser.find_element_by_id("password")
password_box.send_keys("todayismonday1")
password_box.submit()

assert "ninjacoder22" in browser.page_source
# Will throw exception if not in

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "ninjacoder22" in link_label
