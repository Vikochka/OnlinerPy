from selenium.webdriver.common.by import By
from framework.elements.Label import Label


class Locators:
    navigate_header = (By.XPATH, "//span[@class='b-main-navigation__text'][text()='%s']" % ('Каталог'))


class MainMenu:

    @staticmethod
    def navigate_main_header():
        navigate_main_header = Label(Locators.navigate_header)
        navigate_main_header.click()
