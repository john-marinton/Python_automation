from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get('https://gabrielecirulli.github.io/2048/')
elem=driver.find_element_by_tag_name('html')
while True:
   elem.send_keys(Keys.UP)
   time.sleep(1)
   elem.send_keys(Keys.RIGHT)
   time.sleep(1)
   elem.send_keys(Keys.DOWN)
   time.sleep(1)
   elem.send_keys(Keys.LEFT)
   time.sleep(1)
