from framework.elements.Label import Label
from onliner.pageObject.pages.BasePageOnliner import BasePageOnliner
from loguru import logger


class CatalogLocators:
    navigate_menu = "//span[@class='catalog-navigation-classifier__item-title-wrapper'][text()='%s']"
    navigate_section = "//div[@class='catalog-navigation-list__aside-title'][contains(text(),'%s')]"

    catalog_navigation_list = "//span[@class='catalog-navigation-list__dropdown-data']//span[" \
                              "@class='catalog-navigation-list__dropdown-title'][contains(text(),'%s')] "
    catalog_label = "//h1[@class='catalog-navigation__title'][contains(text(),'%s')]"


class CatalogPage(BasePageOnliner):

    def __init__(self, label):
        super().__init__(CatalogLocators.catalog_label % label, "Catalog page")

    @staticmethod
    def navigate_menu(navigate_menu):
        navigate_cat_menu = Label(xpath=CatalogLocators.navigate_menu % navigate_menu)
        navigate_cat_menu.action_click()
        logger.info('Navigate menu header is successful')

    @staticmethod
    def navigate_section(navigate_section):
        navigate_sec = Label(xpath=CatalogLocators.navigate_section % navigate_section)
        navigate_sec.action_click()
        logger.info('Navigate section header is successful')

    @staticmethod
    def navigate_section_list(catalog_navigation_list):
        navigate_section_list = Label(xpath=CatalogLocators.catalog_navigation_list % catalog_navigation_list)
        navigate_section_list.action_click()
        logger.info('Navigate section header click is successful')
