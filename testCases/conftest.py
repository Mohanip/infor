# import parser
# import selenium
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

s = Service('C:/chromedriver_win32/chromedriver.exe')


@pytest.fixture()
def setup(browser):
    # global driver
    #global driver
    if browser == 'chrome':
        driver = webdriver.Chrome(service=s, options=options)
        # driver.back()
        # driver.forward()
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=s, options=options)
    # driver = webdriver.Chrome(service=s, options=options)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # it will return the browser value to setup method.
    return request.config.getoption("--browser")


####################################### Pytest HTML Report ###########################
# It is hook for adding Envir
def pytest_configure(config):
    config._metadata['Project Name'] = 'Sample project'
    config._metadata['Module name'] = 'Customers'
    config._metadata['Tester'] = 'Mohan Periyasamy'


# It is hook for delete/Modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
