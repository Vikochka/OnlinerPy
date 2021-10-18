from framework.elements.Label import Label
from  termcolor import colored
from loguru import logger


class Locators:
    navigate_header = "//span[@class='b-main-navigation__text'][text()='%s']"


class MainMenu:

    @staticmethod
    def navigate_main_header(section):
        navigate_main_header = Label(xpath=Locators.navigate_header % (section))
        navigate_main_header.action_click()
        logger.info(colored('Navigate main header is successful', 'green'))
