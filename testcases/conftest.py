import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from config import RunConfig

capabilities = {
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': 'elly-test',
    'appPackage': RunConfig.appPackage,
    'appActivity': RunConfig.appActivity,
    'appWaitActivity': RunConfig.appWaitActivity,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
}

@pytest.fixture(scope="session")
def launch_app():
    driver = webdriver.Remote(RunConfig.url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.implicitly_wait(4)
    yield driver
    driver.terminate_app(RunConfig.appPackage) #Appium 2.0
    driver.quit()