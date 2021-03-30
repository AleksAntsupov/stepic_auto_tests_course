import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

#Запускаю фикстуру с областью видимости "function".
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()

class TestMainPage():
    def test_guest_should_see_login_link(self,browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
    
    def test_guest_should_see_basket_link__on_the_main_page(self,browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
    
    #Делаю маркировку для пропуска теста, который падает, после этого сделал правильный тест и смотрю на результаты XPASS
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("input.btn.btn-default")