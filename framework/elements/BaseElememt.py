import time
from termcolor import colored

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
from framework.Browser import Browser


class BaseElement(object):
    _locator = ('', '')
    _web_driver = Browser.driver
    _page = None
    _timeout = 10
    _wait_after_click = 3

    def __init__(self, timeout=10, wait_after_click=False, **kwargs):
        self._timeout = timeout
        self._wait_after_click = wait_after_click
        for attr in kwargs:
            self._locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))

    def __getitem__(self, item):
        elements = self.finds()
        return elements[item]

    def find(self, timeout=10):
        element = None
        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.presence_of_element_located(self._locator)
            )
            logger.info(colored('Element found on the page!', 'green'))
            return element
        except:
            logger.error(colored('Element not found on the page!', 'red'))

    def finds(self, timeout=10):
        elements = []
        try:
            elements = WebDriverWait(self._web_driver, timeout).until(
                EC.presence_of_all_elements_located(self._locator)
            )
        except:
            logger.error(colored('Elements not found on the page!', 'red'))
        return elements

    def count(self):
        elements = self.finds()
        return len(elements)

    def get_text_s(self):
        elements = self.finds()
        result = []
        for element in elements:
            text = ''
            try:
                text = str(element.text)
            except Exception as e:
                logger.error(colored('Error: {0}'.format(e), 'red'))
            result.append(text)
        return result

    def wait_to_be_clickable(self, timeout=10, check_visibility=True):
        element = None
        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(self._locator)
            )
            logger.info(colored('Element is clickable', 'green'))
        except:
            logger.error('Element is not clickable!', 'red')
        if check_visibility:
            self.wait_until_not_visible()

        return element

    def is_clickable(self):
        element = self.wait_to_be_clickable()
        logger.info(colored('Element is clickable', 'green'))
        return element is not None

    def is_presented(self):
        element = self.find()
        return element is not None

    def is_visible(self):
        element = self.find()
        if element:
            return element.is_displayed()
        return False

    def wait_until_not_visible(self, timeout=10):
        element = None
        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )

        except:
            logger.error(colored('Element not visible!', 'red'))

        if element:
            js = ('return (!(arguments[0].offsetParent === null) && '
                  '!(window.getComputedStyle(arguments[0]) === "none") &&'
                  'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0'
                  ');')
            visibility = self._web_driver.execute_script(js, element)
            iteration = 0
            while not visibility and iteration < 10:
                time.sleep(0.5)
                iteration += 1
                visibility = self._web_driver.execute_script(js, element)
                logger.info('Element {0} visibility: {1}'.format(self._locator, visibility))
        return element

    def send_keys(self, keys):
        element = self.find()
        if element:
            element.send_keys(keys)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def get_text(self):
        element = self.find()
        text = ''
        try:
            text = str(element.text)
        except Exception as e:
            logger.error(colored('Error: {0}'.format(e), 'red'))
        return text

    def get_attribute(self, attr_name):
        element = self.find()
        if element:
            return element.get_attribute(attr_name)

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset). \
                pause(hold_seconds).click(on_element=element).perform()
            self._page.wait_page_loaded()
        else:
            msg = 'Element not found'
            raise AttributeError(msg.format(self._locator))

        if self._wait_after_click:
            self._page.wait_page_loaded()

    def action_click(self):
        element = self.wait_to_be_clickable()
        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element(element).click().perform()
        else:
            msg = 'Element not found'
            raise AttributeError(msg.format(self._locator))
        if self._wait_after_click:
            self._page.wait_page_loaded()

    def is_selected(self):
        element = self.wait_to_be_clickable()
        if element:
            action = ActionChains(self._web_driver)
            action.click().perform()
            element.is_selected()
            logger.info(colored('Element id selected', 'green'))
        else:
            msg = 'Element is not selected'
            logger.error(colored(msg, 'red'))

        if self._wait_after_click:
            self._page.wait_page_loaded()

    def split(self, param):
        pass

    def highlight_and_make_screenshot(self, file_name):
        element = self.find()
        self._web_driver.execute_script("arguments[0].scrollIntoView();", element)
        self._web_driver.execute_script("arguments[0].style.border='3px solid red'", element)
        self._web_driver.save_screenshot(file_name + '.png')
