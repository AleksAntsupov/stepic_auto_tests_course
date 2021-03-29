import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

#Пишем фикстуру, которая будет при каждом тесте открывать свой браузер
@pytest.fixture
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    return browser

class TestMainPage():
    #вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self,browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
    
    def test_guest_should_see_basket_link__on_the_main_page(self,browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
