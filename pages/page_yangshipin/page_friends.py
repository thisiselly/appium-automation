from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from base.enums import Direction
from pages.page_yangshipin.enums import FriendsCircle
from utils.assert_util import *


class FriendsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_friend_tab()

    # elements
    channel_id = (AppiumBy.ID, 'channel_id_text')
    friend_button = (AppiumBy.XPATH, '//*[@text="央友圈"]')
    focused_tab = (AppiumBy.XPATH,
                   '//*[@resource-id="com.cctv.yangshipin.app.androidp:id/red_bar"]/preceding-sibling::*[@resource-id="com.cctv.yangshipin.app.androidp:id/channel_id_text"]')

    def go_to_friend_tab(self):
        self.click(self.friend_button)

    def verify_text_in_friend_page(self):
        actual_texts = self.get_all_texts(self.channel_id)
        assert_true(len(actual_texts) == 3, "fail")
        assert_true(actual_texts[0] == FriendsCircle.square.value, "fail")
        assert_true(actual_texts[1] == FriendsCircle.my_circle.value, "fail")
        assert_true(actual_texts[2] == FriendsCircle.hot_topics.value, "fail")

    def get_focused_tab_name(self):
        return self.get_text(self.focused_tab)

    def swipe_to_right_tab(self):
        self.swipe_from_left_to_right()

    def verify_swipe_to_diff_tabs(self):
        default_tab = self.get_focused_tab_name()
        assert_equal(default_tab, FriendsCircle.square.value, "default tab is not correct")
        self.swipe(Direction.TO_LEFT)
        current_tab = self.get_focused_tab_name()
        assert_equal(current_tab, FriendsCircle.my_circle.value, "focused tab not correct after swipe")
        self.swipe(Direction.TO_LEFT)
        current_tab = self.get_focused_tab_name()
        assert_equal(current_tab, FriendsCircle.hot_topics.value, "focused tab not correct after swipe")
