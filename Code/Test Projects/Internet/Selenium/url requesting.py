from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe') # don't touch
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfspN-rlguXYI2o59DCqCQlobdVy6Q0PnTqhfP36LUYJychdg/viewform?usp=sf_link')
# wait for the page to load everything (works without it)
for i in range(2):
    print(i)
    time.sleep(1)
while True:
    all_options = driver.find_elements_by_id("i5")
    for option in all_options:
        print("Value is: %s" % option.get_attribute("value"))
        option.click()
    all_options2 = driver.find_elements_by_id("i12")
    for option2 in all_options2:
        print("Value is: %s" % option2.get_attribute("value"))
        option2.click()
    time.sleep(0.1)
#submit = driver.find_elements_by_tag_name("button")
#submit.click()
