from onliner.pageObject.pages.BasePageOnliner import BasePageOnliner


class Locators:
    page_locator = "//div[@class='g-top-i']//img[@class='onliner_logo']"


class MainPage(BasePageOnliner):

    def __init__(self):
        super().__init__(Locators.page_locator, "Main page")
