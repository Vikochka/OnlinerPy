import pytest

from onliner.pageObject.pages.MainPage import MainPage
from onliner.pageObject.pages.catalog_page import CatalogPage
from onliner.pageObject.pages.tv_page import TVPage


def test_onliner(browser):
    main = MainPage()
    main.main_menu.navigate_main_header('Каталог')

    catalog = CatalogPage('Каталог')
    catalog.navigate_menu('Электроника')
    catalog.navigate_section('Телевидение')
    catalog.navigate_section_list('Телевизоры')

    tv_page = TVPage('Телевизоры')
    tv_page.select_manufacturer('Samsung')
    tv_page.select_resolution('1920x1080 (Full HD)')
    tv_page.select_diagonal("40", "50")
    tv_page.select_price(1000)
    tv_page.check_manufacturer("Samsung")
    tv_page.check_resolution("1920x1080 (Full HD)")
    tv_page.check_price(1000.00)
    tv_page.check_diagonal()


