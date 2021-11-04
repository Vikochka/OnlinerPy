import pytest

from onliner.pageObject.pages.MainPage import MainPage
from onliner.pageObject.pages.СatalogPage import CatalogPage
from onliner.pageObject.pages.TvPage import TVPage
from loguru import logger


# logger.add("console.log", format="{time} {level} {message}")


@pytest.mark.parametrize("tv,manufacturer,price,resolution,diagonal_from,diagonal_to",
                         [('Телевизоры', 'Samsung', 1000,
                           '1920x1080 (Full HD)', 40, 50)])
def test_onliner(browser, tv, manufacturer, price, resolution, diagonal_from,
                 diagonal_to):
    main = MainPage()
    main.main_menu.navigate_main_header('Каталог')

    catalog = CatalogPage('Каталог')
    catalog.navigate_menu('Электроника')
    catalog.navigate_section('Телевидение')
    catalog.navigate_section_list('Телевизоры')

    tv_page = TVPage('Телевизоры')
    tv_page.select_manufacturer(manufacturer)
    tv_page.select_price(price)
    tv_page.select_diagonal(diagonal_from, diagonal_to)
    tv_page.select_resolution(resolution)

    tv_page.check_manufacturer(manufacturer)
    tv_page.check_resolution(resolution)
    tv_page.check_price(price)
    tv_page.check_diagonal(diagonal_from, diagonal_to)
