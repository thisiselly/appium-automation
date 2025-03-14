from pages.page_yangshipin.page_live import LivePage


class TestLive:

    def test_switch_to_live_tab(self, launch_yang):
        live_page = LivePage(launch_yang)
        live_page.verify_text_in_live_page()