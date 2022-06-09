from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from selenium import webdriver

list_url=[]
class EnterPage(BasePage):
    def should_be_header(self):
        assert self.is_element_present(*MainPageLocators.HEADER), "Шапка не найдена"
    
    def should_be_footer(self):
        assert self.is_element_present(*MainPageLocators.FOOTER), "Подвал не найден"

    def get_all_link(self):
        global list_url
        elems = self.browser.find_elements(by=By.XPATH, value="//a[@href]")
        for elem in elems:
            list_url.append(elem.get_attribute("href"))
        assert len(list_url)==200, f"На самом деле их 280, а не {len(list_url)}"

    def open_all_link(self):
        new_window = webdriver.Chrome()
        for i in list_url:
            new_window.get(i)
            if i != new_window.current_url:
                print(f'{i} не совпадает с урл {new_window.current_url}')
            continue
            
