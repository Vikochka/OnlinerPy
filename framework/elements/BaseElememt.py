from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.Browser import Browser


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
        self.find_element(locator=self.element)
        self.element.click()

    def action_click(self):
        self.find_element(locator=self.element)
        actions = ActionChains(Browser().driver)
        actions.click(self.element)
        actions.perform()

    def is_displayed(self):
        self.find_element(locator=self.element)
        self.element.is_displayed()

    def send_keys(self, text):
        self.find_element(locator=self.element)
        self.element.send_keys(text)

    def get_text(self):
        self.find_element(locator=self.element)
        return self.element.text()


