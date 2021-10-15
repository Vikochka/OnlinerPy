from framework.elements.Label import Label
from loguru import logger

class BasePage:
    def __init__(self, title_locator, title):
        self.title_locator = title_locator
        self.assert_is_open(title)

    def assert_is_open(self, title):
        label = Label(self.title_locator)
        try:
            label.get_elements()
            logger.info(f"Page {title} opens")
        except:
            logger.error(f"Page {title} does not open")
