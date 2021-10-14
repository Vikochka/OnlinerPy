from selenium.webdriver.common.by import By

from framework.BasePage import BasePage
from framework.elements.Label import Label


class Locators:
    navigate_header = (By.XPATH, "//span[@class='b-main-navigation__text'][text()='Каталог']")
    page_locator = (By.XPATH, "//div[@class='g-top-i']//img[@class='onliner_logo']")


class MainPage(BasePage):
    def __init__(self):
        super().__init__(Locators.page_locator, "Main page")

    @staticmethod
    def navigate_main_header():
        navigate_main_header = Label(Locators.navigate_header)
        navigate_main_header.click()
