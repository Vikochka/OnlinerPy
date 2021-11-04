from framework.elements.Label import Label
from loguru import logger


class BasePage:
    def __init__(self, title_locator, title):
        self.assert_is_open(title_locator, title)

    @staticmethod
    def assert_is_open(title_locator, title):
        label = Label(xpath=title_locator)
        try:
            label.is_visible()
            logger.info(f"{title} opens")
        except:
            logger.error(f"{title} does not open")
