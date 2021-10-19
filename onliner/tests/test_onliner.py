import pytest

from onliner.pageObject.pages.MainPage import MainPage
from onliner.pageObject.pages.catalog_page import CatalogPage
from onliner.pageObject.pages.tv_page import TVPage


@pytest.mark.parametrize("catalog,electronics,television,tv,manufacturer,price,resolution,diagonal_from,diagonal_to",
                         [('Каталог', 'Электроника', 'Телевидение', 'Телевизоры', 'Samsung', 1000,
                           '1920x1080 (Full HD)', 40, 50)])
def test_onliner(browser, catalog, electronics, television, tv, manufacturer, price, resolution, diagonal_from,
                 diagonal_to):
    main = MainPage()
    main.main_menu.navigate_main_header(catalog)

    catalog = CatalogPage(catalog)
    catalog.navigate_menu(electronics)
    catalog.navigate_section(television)
    catalog.navigate_section_list(tv)

    tv_page = TVPage(tv)
    tv_page.select_manufacturer(manufacturer)
    tv_page.select_price(price)
    tv_page.select_diagonal(diagonal_from, diagonal_to)
    tv_page.select_resolution(resolution)

    tv_page.check_manufacturer(manufacturer)
    tv_page.check_price(price)
    tv_page.check_diagonal(diagonal_from, diagonal_to)
    tv_page.check_resolution(resolution)
