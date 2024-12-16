import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
Selain = webdriver.Edge()

Selain.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(25)
Cookie = Selain.find_element(By.ID, "bigCookie")

while True: 
    Cookie.click()