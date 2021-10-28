from framework.elements.CheckBox import CheckBox
from framework.elements.TextBox import TextBox
from onliner.pageObject.pages.BasePageOnliner import BasePageOnliner
from loguru import logger
from termcolor import colored


class TVPageLocators:
    manufacturer = "//label[@class='schema-filter__checkbox-item']//span[text()='%s']/../span[@class='i-checkbox']"

    diagonal_from = "//div[contains(@class,'schema-filter__label')]/..//div[@class='schema-filter-control " \
                    "schema-filter-control_select']//select[contains(@data-bind,'value: facet.value.from')] "
    diagonal_to = "//div[contains(@class,'schema-filter__label')]/..//div[@class='schema-filter-control " \
                  "schema-filter-control_select']//select[contains(@data-bind,'value: facet.value.to')] "

    price_to = "//div[contains(@class,'schema-filter__label')]/..//div[@class='schema-filter__facet']//input[" \
               "contains(@placeholder,'до')] "
    resolution = "//span[contains(@class,'schema-filter__checkbox-text')][text()='%s']/../span[" \
                 "@class='i-checkbox'] "

    price_check = "//div[@class='schema-product__group']//div[contains(@class,'schema-product__price')]//span[" \
                  "contains(@data-bind,'format.minPrice')] "
    block = "//div[@id='schema-products']//div[contains(@class,'schema-product__part schema-product__part_2')]"

    title_check = "//div[@id='schema-products']//div[contains(@class,'schema-product__title')]"

    scheme_products = "//div[@class='schema-product']"

    description = "//div[@class='schema-product__description']"

    pageLocator = "//h1[contains(@class,'schema-header__title')][contains(text(),'%s')]"


class TVPage(BasePageOnliner):

    def __init__(self, label):
        super().__init__(TVPageLocators.pageLocator % label, "ТV page")

    @staticmethod
    def select_manufacturer(select_manufacturer):
        man = CheckBox(xpath=TVPageLocators.manufacturer % select_manufacturer)
        man.action_click()
        logger.info(colored('Manufacturer was selected successful', 'green'))

    @staticmethod
    def select_diagonal(d_from, d_to):
        diag_from = TextBox(xpath=TVPageLocators.diagonal_from)
        diag_to = TextBox(xpath=TVPageLocators.diagonal_to)
        diag_from.send_keys(d_from)
        diag_to.send_keys(d_to)
        logger.info(colored('Diagonal was selected successful', 'green'))

    @staticmethod
    def select_price(price):
        price_to = TextBox(xpath=TVPageLocators.price_to)
        price_to.send_keys(price)
        logger.info(colored('Price was selected successful', 'green'))

    @staticmethod
    def select_resolution(select_resolution):
        res = CheckBox(xpath=TVPageLocators.resolution % select_resolution)
        res.action_click()
        res.is_selected()
        logger.info(colored('Resolution was selected successful', 'green'))

    @staticmethod
    def check_price(price_to):
        block = TextBox(xpath=TVPageLocators.block)
        price = TextBox(xpath=TVPageLocators.price_check)
        for i in range(0, block.count(), +1):
            price_arr = price.get_text().split(" ")
            price_check = price_arr[0].replace(',', '.')
            if float(price_check) <= price_to:
                logger.info(colored('Price is correct', 'green'))
                return True
            else:
                logger.info(colored('Price is not correct: ' + price_check, 'red'))
                return False

    @staticmethod
    def check_manufacturer(man):
        block = TextBox(xpath=TVPageLocators.block).count()
        print(block)
        title_check = TextBox(xpath=TVPageLocators.title_check)
        for i in range(0, block, +1):
            title = title_check.get_text()
            title_split = title.split()
            manufacturer_get = title_split[1]
            if manufacturer_get == man:
                logger.info(colored('Manufacturer is correct', 'green'))
                return True
            else:
                logger.error(colored("Manufacturer is not correct: " + manufacturer_get, 'red'))
                return False

    @staticmethod
    def check_diagonal(d_from, d_to):
        scheme_products = TextBox(xpath=TVPageLocators.scheme_products).count()
        description = TextBox(xpath=TVPageLocators.description)
        for i in range(0, scheme_products, +1):
            description_item = description.get_text()
            des_split = description_item.split('"')
            if d_from <= int(des_split[0]) <= d_to:
                logger.info(colored('Diagonal is correct', 'green'))
                return True
            else:
                logger.error(colored('Diagonal is not correct: ' + des_split[0], 'red'))
                return False

    @staticmethod
    def check_resolution(res):
        scheme_products = TextBox(xpath=TVPageLocators.scheme_products)
        description = TextBox(xpath=TVPageLocators.description)
        for i in range(0, scheme_products.count(), +1):
            description_item = description.get_text().split('" ')
            resolution = description_item[1].split(",")
            if resolution[0] == res:
                logger.info(colored('Resolution is correct', 'green'))
                return True
            else:
                logger.error(colored('Resolution is not correct: ' + resolution[0], 'red'))
                return False
