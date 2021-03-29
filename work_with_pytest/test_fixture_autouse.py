import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

#Запускаю фикстуру на открытие/закрытие окна браузера при каждом тесте
@pytest.fixture
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()
    
#Запускаю фикстуру autouse для каждого теста без явного вызова
@pytest.fixture(autouse = True)
def prepare_data():
    print()
    print("preparing some critical data for every test")

class TestMainPage():
    #вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self,browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")
    
    def test_guest_should_see_basket_link__on_the_main_page(self,browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")