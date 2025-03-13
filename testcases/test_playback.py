import time

from pages.page_play import PlayPage
from pages.page_search import SearchPage


class TestPlayback:
    def test_progressbar_dismiss(self, launch_app):
        search_string = "宝宝巴士"
        search_page = SearchPage(launch_app)
        search_page.search_for_content(search_string)
        search_page.select_search_poster()
        play_page = PlayPage(launch_app)
        play_page.verify_progressbar_shown(expect_found=True)
        time.sleep(10)
        play_page.verify_progressbar_shown(expect_found=False)
        play_page.click_on_playing_view()
        play_page.verify_progressbar_shown(expect_found=True)

