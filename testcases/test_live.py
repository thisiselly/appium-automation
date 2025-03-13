from pages.page_live import LivePage


class TestLive:

    def test_switch_to_live_tab(self, launch_app):
        live_page = LivePage(launch_app)
        live_page.verify_text_in_live_page()