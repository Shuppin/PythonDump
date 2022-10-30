from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(chrome_options=options)
for i in range(10):
    driver.execute_script('''window.open("https://youtube.com","_blank");''')
    print(f"Script {i+1} passed") 

time.sleep(2)

driver.close()

