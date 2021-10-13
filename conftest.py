import pytest

from framework.Browser import Browser


@pytest.fixture(scope="session")
def browser():
    driver = Browser()
    driver.instance()
    driver.maximize_window()
    driver.implicitly_wait()
    driver.get()
    yield driver
    driver.quit()
