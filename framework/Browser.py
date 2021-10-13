import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from framework.driver_factory import WebDriverFactory
from selenium import webdriver


class Browser:
    driver = webdriver

    def __init__(self):
        self.driver = self.driver
        self.base_url = "https://www.onliner.by/"

    def instance(self):
        self.driver = WebDriverFactory().getWebDriverInstance("chrome")

    def maximize_window(self):
        return self.driver.maximize_window()

    def implicitly_wait(self):
        return self.driver.implicitly_wait(20)

    def get(self):
        return self.driver.get(self.base_url)

    def quit(self):
        return self.driver.quit()

    def wait_page_loaded(self, timeout=10, check_js_complete=True,
                         check_page_changes=False,
                         wait_for_element=None,
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

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self.driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element._locator)
                    )
                except:
                    pass

            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        self.driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
