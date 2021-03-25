from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button1 = browser.find_element_by_xpath("//button[contains(@class,'btn-primary')]")
    button1.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    button2 = browser.find_element_by_xpath("//button[contains(@class,'btn-primary')]")
    button2.click()
finally:
    time.sleep(7)
    browser.quit()