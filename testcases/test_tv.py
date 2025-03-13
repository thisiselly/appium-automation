from pages.page_tv import TVPage


class TestTV:

    def test_switch_to_tv_tab(self, launch_app):
        tv_page = TVPage(launch_app)
        tv_page.verify_text_in_tv_page()