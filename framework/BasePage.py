from framework.elements.Label import Label
from loguru import logger
from termcolor import colored


class BasePage:
    def __init__(self, title_locator, title):
        self.assert_is_open(title_locator, title)

    @staticmethod
    def assert_is_open(title_locator, title):
        label = Label(xpath=title_locator)
        try:
            label.is_visible()
            logger.info(colored(f"{title} opens", 'green'))
        except:
            logger.error(colored(f"{title} does not open", 'red'))
