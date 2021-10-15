from selenium import webdriver
from loguru import logger
import json

from framework.property_reader import PropertyReader


class WebDriverFactory:
    driver = None
    prop = PropertyReader()

    def getWebDriverInstance(self):
        prop_browser = self.prop.get_property('C://Users//V.Yermakovich//PycharmProjects//Onliner//config.properties', 'browser')
        if prop_browser == "firefox":
            self.driver = webdriver.Firefox(executable_path="C://Install//geckodriver-v0.29.1-win64//gekodriver.exe")
            logger.info(f"{prop_browser} browser was opened")
        if prop_browser == "chrome":
            self.driver = webdriver.Chrome(executable_path="C://Install//chromedriver_win32//chromedriver.exe")
            logger.info(f"{prop_browser} browser was opened")
        else:
            logger.error(f"Can't find browser: {prop_browser}")
        return self.driver
