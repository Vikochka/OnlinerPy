from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.Browser import Browser
from loguru import logger


class BaseElement:
    element = WebElement

    def __init__(self, element):
        self.element = element

    def find_element(self, locator, time=10):
        self.element = WebDriverWait(Browser().driver, time).until(EC.presence_of_element_located(locator),
                                                                   message=f"Can't find element by locator {locator}")
        return self.element

    def find_elements(self, locator, time=10):
        self.element = WebDriverWait(Browser().driver, time).until(EC.presence_of_all_elements_located(locator),
                                                                   message=f"Can't find elements by locator {locator}")
        return self.element

    def get_elements(self):
        # self.find_elements(locator=self.element)
        return self.find_elements(locator=self.element)

    def get_element(self):
        # self.find_elements(locator=self.element)
        return self.find_element(locator=self.element)

    def click(self):
        try:
            self.find_element(locator=self.element)
            self.element.click()
            logger.info(f"Clicking on an element was successful")
        except:
            logger.error(f"Clicking on an element was not successful")

    def action_click(self):
        try:
            self.find_element(locator=self.element)
            actions = ActionChains(Browser().driver)
            actions.click(self.element)
            actions.perform()
            logger.info(f"Clicking on an element was successful")
        except:
            logger.error(f"Clicking on an element was not successful")

    def is_displayed(self):
        self.find_element(locator=self.element)
        self.element.is_displayed()

    def send_keys(self, text):
        try:
            self.find_element(locator=self.element)
            self.element.send_keys(text)
            logger.info(f"{text} was enter successful")
        except:
            logger.info(f"{text} was not enter successful")

    def get_text(self):
        try:
            self.find_element(locator=self.element)
            text = self.element.text
            logger.info(f"Text of element" + text)
        except:
            logger.error("Text error")