from selenium.webdriver.common.by import By

from framework.BaseApp import BasePage
from framework.Browser import Browser


class Locators:
    navigate_header = (By.XPATH, "//span[@class='b-main-navigation__text'][text()='Каталог']")


class MainPage(Browser):

    def navigate_main_header(self):
        navigate_main_header = self.find_element(Locators.navigate_header)
        navigate_main_header.click()
