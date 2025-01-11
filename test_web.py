from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

os.system('cls')

# driver = webdriver.Firefox()
print('Program Ran!')

driver = webdriver.Chrome()


# driver.get("https://divar.ir/s/mashhad/buy-apartment/abkuh")

Cookies = driver.get_cookies()

print(Cookies)