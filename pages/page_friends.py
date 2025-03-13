from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from utils.assert_util import *


class FriendsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_friend_tab()

    # elements
    friend_button = (AppiumBy.XPATH, '//*[@text="央友圈"]')
    friend_playground = (AppiumBy.XPATH, '//*[@text="广场"]')
    friend_my_circle = (AppiumBy.XPATH, '//*[@text="我的圈子"]')
    friend_hot_topic = (AppiumBy.XPATH, '//*[@text="热门话题"]')

    def go_to_friend_tab(self):
        self.click(self.friend_button)

    def verify_text_in_friend_page(self):
        text1_displayed = self.element_exist(self.friend_playground)
        text2_displayed = self.element_exist(self.friend_my_circle)
        text3_displayed = self.element_exist(self.friend_hot_topic)
        assert_true(text1_displayed == text2_displayed == text3_displayed == True, "the expect elements are not shown")
