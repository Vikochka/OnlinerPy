import os

from selenium import webdriver
from loguru import logger
from framework.property_reader import PropertyReader
from termcolor import colored


class WebDriverFactory:
    driver = None
    prop = PropertyReader()

    def getWebDriverInstance(self):
        prop_browser = self.prop.get_property('../config.properties',
                                              'browser')
        if prop_browser == "firefox":
            self.driver = webdriver.Firefox(executable_path="C://Install//geckodriver-v0.29.1-win64//gekodriver.exe")
            logger.info(colored(f"{prop_browser} browser was opened", 'green'))
        if prop_browser == "chrome":
            self.driver = webdriver.Chrome(executable_path="C://Install//chromedriver_win32//chromedriver.exe")
            logger.info(colored(f"{prop_browser} browser was opened", 'green'))
        else:
            logger.error(colored(f"Can't find browser: {prop_browser}", 'red'))
        return self.driver
