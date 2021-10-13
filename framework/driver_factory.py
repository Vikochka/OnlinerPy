from selenium import webdriver


class WebDriverFactory:
    driver = None

    def getWebDriverInstance(self, prop_browser):
        if prop_browser == "firefox":
            self.driver = webdriver.Firefox(executable_path="C://Install//geckodriver-v0.29.1-win64//gekodriver.exe")
        if prop_browser == "chrome":
            self.driver = webdriver.Chrome(executable_path="C://Install//chromedriver_win32//chromedriver.exe")
        else:
            print(f"Can't find browser: {prop_browser}")
        return self.driver
