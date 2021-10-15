from selenium.webdriver.common.by import By

from framework.BasePage import BasePage
from framework.elements.CheckBox import CheckBox
from framework.elements.TextBox import TextBox
from onliner.pageObject.pages.BasePageOnliner import BasePageOnliner


class TVPageLocators:
    manufacturer = (By.XPATH, "//label[@class='schema-filter__checkbox-item']"
                              "//span[text()='Samsung']/../span[@class='i-checkbox']")

    diagonal_from = (By.XPATH, "//div[contains(@class,'schema-filter__label')]/..//div"
                               "[@class='schema-filter-control schema-filter-control_select']//"
                               "select[contains(@data-bind,'value: facet.value.from')]")
    diagonal_to = (By.XPATH, "//div[contains(@class,'schema-filter__label')]/..//div"
                             "[@class='schema-filter-control schema-filter-control_select']//select"
                             "[contains(@data-bind,'value: facet.value.to')]")

    price_to = (By.XPATH, "//div[contains(@class,'schema-filter__label')]/..//div"
                          "[@class='schema-filter__facet']//input[contains(@placeholder,'до')]")
    resolution = (By.XPATH, "//ul[@class='schema-filter__list']//label"
                            "[contains(@class,'schema-filter__checkbox-item')]//"
                            "span[contains(@class,'schema-filter__checkbox-text')][text()='1920x1080 (Full HD)'] ")

    price_check = (By.XPATH, "//div[@class='schema-product__group']//div[contains(@class,"
                             "'schema-product__price')]//span[contains(@data-bind,'format.minPrice')]")
    block = (
        By.XPATH, "//div[@id='schema-products']//div[contains(@class,'schema-product__part schema-product__part_2')]")

    title_check = (By.XPATH, "//div[@id='schema-products']//div[contains(@class,'schema-product__title')]")

    scheme_products = (By.XPATH, "//div[@class='schema-product']")

    description = (By.XPATH, "//div[@class='schema-product__description']")

    pageLocator = (By.XPATH, "//h1[contains(@class,'schema-header__title')][contains(text(),'Телевизоры')]")


class TVPage(BasePageOnliner):

    def __init__(self):
        super().__init__(TVPageLocators.pageLocator, "ТV page")

    @staticmethod
    def select_manufacturer():
        man = CheckBox(TVPageLocators.manufacturer)
        man.click()

    @staticmethod
    def select_diagonal(d_from, d_to):
        diag_from = TextBox(TVPageLocators.diagonal_from)
        diag_to = TextBox(TVPageLocators.diagonal_to)
        diag_from.send_keys(d_from)
        diag_to.send_keys(d_to)

    @staticmethod
    def select_price(price):
        price_to = TextBox(TVPageLocators.price_to)
        price_to.send_keys(price)

    @staticmethod
    def select_resolution():
        res = CheckBox(TVPageLocators.resolution)
        res.action_click()

    @staticmethod
    def check_price(price):
        block = TextBox(TVPageLocators.block).get_elements()
        for i in range(0, len(block), 1):
            price_arr = TextBox(TVPageLocators.price_check).get_text().split(",")
            price_int = int(price_arr[0])
            print(price_int)
            if price_int <= price:
                return True
            else:
                return False

    @staticmethod
    def check_manufacturer(man):
        block = TextBox(TVPageLocators.block).get_elements()
        print(len(block))
        title_check = TextBox(TVPageLocators.title_check).get_elements()
        print(title_check)
        for i in range(0, len(block), 1):
            title = title_check[i].get_text()
            print(title)
        #     title_split = title.split()
        #     manufacturer_get = title_split[1]
        #     if manufacturer_get == man:
        #         return True
        #     else:
        #         return False

    @staticmethod
    def check_diagonal():
        scheme_products = TextBox(TVPageLocators.scheme_products).get_elements()
        print(len(scheme_products))
        description = TextBox(TVPageLocators.description).get_elements()

        for i in range(0, len(scheme_products), +1):
            description_item = description[i].get_text()
            print(description_item)
            des_split = description_item.split(" ")
            description_arr = list[des_split]
            print(description_arr)
            assert 40 <= int(des_split[0]) <= 50

    @staticmethod
    def check_resolution(res):
        scheme_products = TextBox(TVPageLocators.scheme_products).get_text()
        print(len(scheme_products))
        description = TextBox(TVPageLocators.description).get_text()

        for i in range(0, len(scheme_products), +1):
            description_item = description[i].get_text()
            print(description_item)
            des_split = description_item.split(" ")
            description_arr = list[des_split]
            print(description_arr)
            assert des_split[i] == res
