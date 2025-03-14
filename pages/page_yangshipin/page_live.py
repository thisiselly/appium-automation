from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from utils.assert_util import *


class LivePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_live_tab()

    # live elements
    live_button = (AppiumBy.XPATH, '//*[@text="直播"]')
    live_top_left_text = (AppiumBy.ID, 'head_title')

    def go_to_live_tab(self):
        self.click(self.live_button)

    def verify_text_in_live_page(self):
        actual_displayed = self.element_exist(self.live_top_left_text)
        assert_true(actual_displayed, "the expect element is not shown")