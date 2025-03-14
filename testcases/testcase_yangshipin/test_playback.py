import time

from pages.page_yangshipin.page_play import PlayPage
from pages.page_yangshipin.page_search import SearchPage


class TestPlayback:
    def test_progressbar_dismiss(self, launch_yang):
        search_string = "宝宝巴士"
        search_page = SearchPage(launch_yang)
        search_page.search_for_content(search_string)
        search_page.select_search_poster()
        play_page = PlayPage(launch_yang)
        play_page.verify_progressbar_shown(expect_found=True)
        time.sleep(10)
        play_page.verify_progressbar_shown(expect_found=False)
        play_page.click_on_playing_view()
        play_page.verify_progressbar_shown(expect_found=True)
        play_page.back(2)

    def test_play_video_success(self, launch_yang):
        search_string = "周杰伦"
        search_page = SearchPage(launch_yang)
        search_page.search_for_content(search_string)
        search_page.select_search_poster()
        play_page = PlayPage(launch_yang)
        play_page.verify_video_is_playing()
        play_page.back(2)

    def test_paused_video_success(self, launch_yang):
        search_string = "周杰伦"
        search_page = SearchPage(launch_yang)
        search_page.search_for_content(search_string)
        search_page.select_search_poster()
        play_page = PlayPage(launch_yang)
        play_page.pause_video_during_playback()
        play_page.verify_video_is_paused()
        play_page.play_video_after_paused()
        play_page.verify_video_is_playing()
