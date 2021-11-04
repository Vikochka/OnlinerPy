from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from framework.DriverFactory import WebDriverFactory
from loguru import logger

from framework.PropertyReader import PropertyReader


class Browser:
    driver = WebDriverFactory().getWebDriverInstance()
    timeout = PropertyReader().get_property(
        '..//config.properties', 'timeout_for_driver')

    def __init__(self):
        self.base_url = PropertyReader().get_property(
            '..//config.properties', 'base_url')

    def instance(self):
        return self.driver

    def maximize_window(self):
        return self.driver.maximize_window()

    def implicitly_wait(self):
        return self.driver.implicitly_wait(self.timeout)

    def get(self):
        try:
            self.driver.get(self.base_url)
            logger.info(f"Browser has opened: {self.base_url}")
            self.wait_page_loaded()
            return self.driver
        except:
            logger.error(f"Browser could not open: {self.base_url}")

    def quit(self):
        self.driver.quit()
        logger.info(f"Browser was closed")

    def wait_page_loaded(self, check_js_complete=True,
                         check_page_changes=False,
                         wait_for_xpath_to_disappear=''):
        page_loaded = False
        double_check = False
        k = 0
        source = ''
        try:
            source = self.driver.page_source
        except:
            pass
        while not page_loaded:
            self.implicitly_wait()
            k += 1
            if check_js_complete:
                try:
                    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self.driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass
            if page_loaded and check_page_changes:
                new_source = ''
                try:
                    new_source = self.driver.page_source
                except:
                    pass
                page_loaded = new_source == source
                source = new_source
            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None
                try:
                    bad_element = WebDriverWait(self.driver, self.timeout).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass
                page_loaded = not bad_element
            assert k < self.timeout, 'The page loaded more than {0} seconds!'.format(self.timeout)
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True
        self.driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
