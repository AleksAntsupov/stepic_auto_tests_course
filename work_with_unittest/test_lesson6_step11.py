from selenium import webdriver
import time, unittest

class TestRegistationPage(unittest.TestCase):
    def test_page_one(self):
        link = "http://suninjuly.github.io/registration1.html"
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
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    
    def test_page_two(self):
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
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()