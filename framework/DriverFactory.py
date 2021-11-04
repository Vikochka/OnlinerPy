from selenium import webdriver
from loguru import logger
from framework.PropertyReader import PropertyReader
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverFactory:
    driver = None
    prop = PropertyReader()

    def getWebDriverInstance(self):
        prop_browser = self.prop.get_property('../config.properties',
                                              'browser')
        if prop_browser == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            logger.info(f"{prop_browser} browser was opened")
        if prop_browser == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            logger.info(f"{prop_browser} browser was opened")
        else:
            logger.error(f"Can't find browser: {prop_browser}")
        return self.driver
