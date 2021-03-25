from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_xpath("//input[contains(@class,'first') and attribute::required]")
    input1.send_keys("Alex")
    input2 = browser.find_element_by_xpath("//input[contains(@class,'second') and attribute::required]")
    input2.send_keys("Antsupov")
    input3 = browser.find_element_by_xpath("//input[contains(@class,'third') and attribute::required]")
    input3.send_keys("a@mail.ru")
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    time.sleep(5)
    
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(3)
    browser.quit()