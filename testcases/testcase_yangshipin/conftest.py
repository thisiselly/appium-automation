import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.get_file_path_util import get_settings_yaml_path
from utils.read_files import read_yaml_file

settings = read_yaml_file(get_settings_yaml_path())
app_info = settings['apps']['yangshipin']
capabilities = settings['capabilities']
capabilities.update(app_info)
url = settings['connection']['url']

@pytest.fixture(scope="session")
def launch_yang():
    driver = webdriver.Remote(url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.implicitly_wait(4)
    yield driver
    driver.terminate_app(app_info['appPackage'])
    driver.quit()
