from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from utils.assert_util import *


class TVPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_tv_tab()

    # tv elements
    tv_button = (AppiumBy.XPATH, '//*[@text="电视"]')
    tv_top_left_text = (AppiumBy.ID, 'tab_title_name')



    def go_to_tv_tab(self):
        self.click(self.tv_button)

    def verify_text_in_tv_page(self):
        actual_displayed = self.element_exist(self.tv_top_left_text)
        assert_true(actual_displayed, "the expect element is not shown")
