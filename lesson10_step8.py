from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math, time

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    price1 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"), '$100'))
    button1 = browser.find_element_by_xpath("//button[contains(@class,'btn-primary')]")
    button1.click()
    
    robot_box = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_box)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
       
    button2 = browser.find_element_by_id("solve")
    button2.click()
finally:
    time.sleep(7)
    browser.quit()    