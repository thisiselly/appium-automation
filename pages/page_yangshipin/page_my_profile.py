from appium.webdriver.common.appiumby import AppiumBy
from utils.assert_util import *

from base.base_page import BasePage


class MyProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_my_profile_tab()

    # me elements
    my_profile_button = (AppiumBy.XPATH, '//*[@text="我的"]')
    my_profile_login_text = (AppiumBy.ID, 'un_login_text_view')
    my_collection_button = (AppiumBy.XPATH, '//*[@text="收藏"]/parent::*[@resource-id="com.cctv.yangshipin.app.androidp:id/setting_rl"]')
    video_title = (AppiumBy.ID, "item_title")
    video_poster = (AppiumBy.ID, "image_fl")
    text_tip = (AppiumBy.ID, "text_tip")

    def go_to_my_profile_tab(self):
        self.click(self.my_profile_button)

    def verify_text_in_my_profile_page(self):
        actual_displayed = self.element_exist(self.my_profile_login_text)
        assert_true(actual_displayed, "the expect element is not shown")

    def go_to_my_collection(self):
        self.click(self.my_collection_button)

    def get_first_video_in_collection(self):
        return self.get_all_videos_in_collection()[0]

    def get_all_videos_in_collection(self):
        all_ele = self.find_elements(self.video_title)
        all_video_title = []
        for ele in all_ele:
            all_video_title.append(ele.text)
        return all_video_title

    def verify_collection_list(self, video, exist=True):
        if exist:
            actual_video = self.get_first_video_in_collection()
            assert_equal(video, actual_video, "the first video in collection is not the video you just favorite.")
        else:
            if self.is_collection_empty():
                assert_true(True)
            else:
                actual_videos = self.get_all_videos_in_collection()
                assert_not_in(video, actual_videos, "the un-favorite video is still in the list, which is incorrect.")

    def select_first_video_in_collection(self):
        all_ele = self.find_elements(self.video_poster)
        all_ele[0].click()

    def is_collection_empty(self):
        return self.find_element(self.text_tip).text == "暂无内容"

