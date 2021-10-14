from onliner.pageObject.MainPage import MainPage
from onliner.pageObject.catalog_page import CatalogPage
from onliner.pageObject.tv_page import TVPage


def test_onliner(browser):
    main = MainPage()
    main.navigate_main_header()

    catalog = CatalogPage()
    catalog.page_load()
    catalog.navigate_menu()
    catalog.navigate_section()
    catalog.navigate_section_list()

    tv_page = TVPage()
    tv_page.select_manufacturer()
    tv_page.select_resolution()
    tv_page.select_diagonal("40", "50")
    tv_page.select_price(1000)
    # tv_page.check_manufacturer("Samsung")
    # tv_page.check_price(1000)

