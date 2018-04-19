from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome('D:\\studies\\Python\\Selenium\\chromedriver.exe')
driver.get('http://www.facebook.com')

elementl=driver.find_element_by_id('u_0_a')
elementp=driver.find_element_by_link_text('Create a Page')

#----moves or hover to the mentioned element from source to target----#
##hover=ActionChains(driver).drag_and_drop(elementl,elementp).click(elementp).perform()


#----------.move_to_element moves or hover to the mentioned element----#
##hover=ActionChains(driver).move_to_element(element).click(element).perform()
