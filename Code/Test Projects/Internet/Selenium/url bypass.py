from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_capabilities = DesiredCapabilities.CHROME.copy()
desired_capabilities['acceptInsecureCerts'] = True
driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
driver.get('https://discord.com')
print(driver.title)
#driver.close()