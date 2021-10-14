from framework.elements.Label import Label


class BasePage:
    def __init__(self, title_locator, title):
        self.title_locator = title_locator
        self.assert_is_open(title)

    def assert_is_open(self,title):
        label = Label(self.title_locator)
        try:
            label.get_elements()
        except:
            print(title + "  does not open")
