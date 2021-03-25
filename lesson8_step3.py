from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(n1,n2):
    return str(n1 + n2)

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    
    count = calc(num1,num2)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(count)
    
    button = browser.find_element_by_xpath("//button[contains(@class,'btn-default')]")
    button.click()
finally:
    time.sleep(7)
    browser.quit()