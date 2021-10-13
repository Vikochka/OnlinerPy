from onliner.pageObject.MainPage import MainPage


def test_onliner(browser):
    main = MainPage()
    main.navigate_main_header()
