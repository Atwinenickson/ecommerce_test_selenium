from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(20) # seconds
        print("Launching Chrome browser...................")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(20) # seconds
        print("Launching Firefox browser............")
    elif browser == 'brave':
        driver = webdriver.Chrome()
        driver.implicitly_wait(20) # seconds
        print("Launching Brave browser...................")
    elif browser == 'ie':
        driver = webdriver.Ie()
        print("Launching IE browser...................")
    elif browser == 'opera':
        driver = webdriver.Opera()
        driver.implicitly_wait(20) # seconds
        print("Launching Opera browser...................")
    else:
        driver = webdriver.Chrome()
        driver.implicitly_wait(20) # seconds
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



'''
pytest html report
'''
#it is a hook for adding environment info to the html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# it is a hook for delete/modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


 