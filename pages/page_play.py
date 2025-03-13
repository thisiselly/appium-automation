import time

from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from utils.logs_util import logger
from utils.assert_util import *


class PlayPage(BasePage):
    # elements
    fav_button = (AppiumBy.ID, "fav_btn")
    like_button = (AppiumBy.ID, "thumb_view")
    play_view = (AppiumBy.ID, "player_module_mediaplayer_view")
    video_title = (AppiumBy.ID, "main_title")
    bottom_container = (AppiumBy.ID, "sw_bottom_container")
    play_btn = (AppiumBy.ID, "play_btn")
    current_time = (AppiumBy.ID, "current_time")
    total_time = (AppiumBy.ID, "total_time")

    def select_fav_button(self):
        self.wait_for_play_view_displays()
        self.click(self.fav_button)

    def wait_for_play_view_displays(self, timeout=60):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if not self.element_exist(self.play_view):
                logger.info("playback view not loaded, wait for 2 seconds")
                time.sleep(2)
            else:
                return

    def get_play_video_title(self):
        return self.get_text(self.video_title)

    def is_progressbar_shown(self, expect_found=True):
        if not expect_found:
            return self.element_exist(self.bottom_container, retry=1, timeout=10)
        else:
            return self.element_exist(self.bottom_container)

    def click_on_playing_view(self):
        self.click(self.play_view)

    def verify_progressbar_shown(self, expect_found=True):
        if expect_found:
            assert_true(self.is_progressbar_shown(), "progress bar is not shown as expect")
        else:
            assert_false(self.is_progressbar_shown(), "progress bar is shown, but expect not.")

    def pause_video_during_playback(self):
        self.click(self.play_btn)

    def pplay_video_after_paused(self):
        self.click(self.play_btn)


