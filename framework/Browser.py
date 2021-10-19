import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from framework.driver_factory import WebDriverFactory
from loguru import logger

from framework.property_reader import PropertyReader
from termcolor import colored


class Browser:
    driver = WebDriverFactory().getWebDriverInstance()

    def __init__(self):
        self.base_url = PropertyReader().get_property(
            'C://Users//V.Yermakovich//PycharmProjects//Onliner//config.properties', 'base_url')

    def instance(self):
        return self.driver

    def maximize_window(self):
        return self.driver.maximize_window()

    def implicitly_wait(self):
        return self.driver.implicitly_wait(PropertyReader().get_property(
            'C://Users//V.Yermakovich//PycharmProjects//Onliner//config.properties', 'timeout_for_driver'))

    def get(self):
        try:
            self.driver.get(self.base_url)
            logger.info(colored(f"Browser has opened: {self.base_url}", 'green'))
            self.wait_page_loaded()
            return self.driver
        except:
            logger.error(colored(f"Browser could not open: {self.base_url}", 'red'))

    def quit(self):
        self.driver.quit()
        logger.info(colored(f"Browser was closed", 'green'))

    def wait_page_loaded(self, timeout=10, check_js_complete=True,
                         check_page_changes=False,
                         wait_for_xpath_to_disappear='',
                         sleep_time=2):
        page_loaded = False
        double_check = False
        k = 0
        if sleep_time:
            time.sleep(sleep_time)
        source = ''
        try:
            source = self.driver.page_source
        except:
            pass
        while not page_loaded:
            time.sleep(0.5)
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
                    bad_element = WebDriverWait(self.driver, 0.1).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass
                page_loaded = not bad_element
            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True
        self.driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
