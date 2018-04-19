#! python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pynput.keyboard import Key,Controller


keyboard=Controller()

movie_=input('Enter the movie you want to search')
driver=webdriver.Chrome('D:\\studies\\Python\\Selenium\\chromedriver.exe')
driver.get('http://yify.is/')

driver.find_element_by_id('quick-search-input').send_keys(movie_)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div[3]/ul/li/a').click()
elem=driver.find_element_by_xpath('//*[@id="movie-info"]/p/a[2]')
if elem.text=='1080p':
   driver.find_element_by_xpath('//*[@id="movie-info"]/p/a[2]').click()
   keyboard.press(Key.enter)
   keyboard.release(Key.enter)
   print('Downloading 1080p')

else:
   driver.find_element_by_xpath('//*[@id="movie-info"]/p/a[1]').click()
   keyboard.press(Key.enter)
   keyboard.release(Key.enter)
   print('Downloading 720p')
   

   


