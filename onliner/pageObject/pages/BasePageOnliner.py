from framework.BasePage import BasePage
from onliner.pageObject.header.MainMenu import MainMenu


class BasePageOnliner(BasePage):
    main_menu = MainMenu()

    def __init__(self, title_locator, title):
        super().__init__(title_locator, title)
