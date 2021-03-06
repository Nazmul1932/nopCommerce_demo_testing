import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    return driver


# this will get the value from cli
def pytest_addoption(parser):
    parser.addoption("--browser")


# this will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Nazmul'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
