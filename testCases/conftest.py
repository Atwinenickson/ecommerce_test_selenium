from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser...................")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser............")
    elif browser == 'brave':
        driver = webdriver.Chrome()
        print("Launching Brave browser...................")
    elif browser == 'ie':
        driver = webdriver.Ie()
        print("Launching IE browser...................")
    elif browser == 'opera':
        driver = webdriver.Opera()
        print("Launching Opera browser...................")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")