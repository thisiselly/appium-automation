from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from utils.assert_util import *


class HomePage(BasePage):
    # home page buttons
    home_button = (AppiumBy.XPATH, '//*[@text="首页"]')
    home_top_left_text = (AppiumBy.ID, 'logo_iv_name')

    def go_to_home_tab(self):
        self.click(self.home_button)

    def verify_text_in_home_page(self):
        actual_displayed = self.element_exist(self.home_top_left_text)
        assert_true(actual_displayed, "the expect element is not shown")






