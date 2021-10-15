from selenium.webdriver.common.by import By

from framework.BasePage import BasePage
from framework.elements.Label import Label
from onliner.pageObject.pages.BasePageOnliner import BasePageOnliner


class CatalogLocators:
    navigate_menu = (
        By.XPATH, "//span[@class='catalog-navigation-classifier__item-title-wrapper'][text()='Электроника']")
    navigate_section = (
        By.XPATH, "//div[@class='catalog-navigation-list__aside-title'][contains(text(),'Телевидение')]")

    catalog_navigation_list = (By.XPATH, "//span[@class='catalog-navigation-list__dropdown-data']"
                                         "//span[@class='catalog-navigation-list__dropdown-title']"
                                         "[contains(text(),'Телевизоры')]")
    catalog_label = (By.XPATH, "//h1[@class='catalog-navigation__title'][contains(text(),'Каталог')]")


class CatalogPage(BasePageOnliner):

    def __init__(self,):
        super().__init__(CatalogLocators.catalog_label, "Catalog page")

    @staticmethod
    def page_load():
        load = Label(CatalogLocators.catalog_label)
        load.is_displayed()

    @staticmethod
    def navigate_menu():
        navigate_cat_menu = Label(CatalogLocators.navigate_menu)
        navigate_cat_menu.click()

    @staticmethod
    def navigate_section():
        navigate_sec = Label(CatalogLocators.navigate_section)
        navigate_sec.click()

    @staticmethod
    def navigate_section_list():
        navigate_section_list = Label(CatalogLocators.catalog_navigation_list)
        navigate_section_list.click()
