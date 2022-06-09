from .page.register_page import EnterPage
import pytest
import allure

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.test                                  
def test_main_page_header_and_footer(browser):
    link = "https://www.mos.ru/"  #открываем
    page = EnterPage(browser, link)
    page.open()
    browser.implicitly_wait(5)
    page.should_be_header()             #провряем раз
    page.should_be_footer()             #провряем два
    page.get_all_link()                 #получаем ссылки

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.test  
@pytest.mark.xfail                                
def test_get_all_page(browser):
    link = "https://www.mos.ru/"  #открываем
    page = EnterPage(browser, link)
    page.open()
    browser.implicitly_wait(5)
    page.get_all_link()                 #получаем ссылки и проверяем количество

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.test   
def test_go_to_link_page(browser):
    link = "https://www.mos.ru/"  #стртовая страница талон
    page = EnterPage(browser, link)
    page.open()
    browser.implicitly_wait(5)
    page.open_all_link()                #переходим по ним и проверяем 
    