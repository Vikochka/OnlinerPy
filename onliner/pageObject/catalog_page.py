from selenium.webdriver.common.by import By

from framework.BasePage import BasePage
from framework.elements.BaseElememt import BaseElement
from framework.elements.Label import Label


class CatalogLocators:
    navigate_menu = (
        By.XPATH, "//span[@class='catalog-navigation-classifier__item-title-wrapper'][text()='Электроника']")
    navigate_section = (
        By.XPATH, "//div[@class='catalog-navigation-list__aside-title'][contains(text(),'Телевидение')]")

    catalog_navigation_list = (By.XPATH, "//span[@class='catalog-navigation-list__dropdown-data']"
                                         "//span[@class='catalog-navigation-list__dropdown-title']"
                                         "[contains(text(),'Телевизоры')]")
    catalog_label = (By.XPATH, "//h1[@class='catalog-navigation__title'][contains(text(),'Каталог')]")


class CatalogPage(BasePage):
    def __init__(self, title_locator, title):
        super().__init__(title_locator, title)

    def page_load(self):
        load = Label(CatalogLocators.catalog_label)
        load.is_displayed()

    def navigate_menu(self):
        navigate_cat_menu = Label(CatalogLocators.navigate_menu)
        navigate_cat_menu.click()

    def navigate_section(self):
        navigate_sec = Label(CatalogLocators.navigate_section)
        navigate_sec.click()

    def navigate_section_list(self):
        navigate_section_list = Label(CatalogLocators.catalog_navigation_list)
        navigate_section_list.click()
