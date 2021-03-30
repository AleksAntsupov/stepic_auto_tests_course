import pytest
from selenium import webdriver
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser...")
    browser.quit()

@pytest.mark.parametrize('url',["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestWithPar():
    def test(self,browser,url):
        browser.get(url)
        
        answer = math.log(int(time.time()+2))
        
        input1 = browser.find_element_by_xpath("//textarea[contains(@class, 'string-quiz__textarea')]")
        input1.send_keys(str(answer))
        
        button1 = browser.find_element_by_xpath("//button[contains(@class, 'submit-submission')]")
        button1.click()
        
        answer2 = browser.find_element_by_xpath("//div/*[contains(@class, 'smart-hints__hint')]").text
        
        assert "Correct!" == answer2, print(answer2)
        
        if __name__ == "__main__":
            pytest.main()