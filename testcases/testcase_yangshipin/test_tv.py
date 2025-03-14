from pages.page_yangshipin.page_tv import TVPage


class TestTV:

    def test_switch_to_tv_tab(self, launch_yang):
        tv_page = TVPage(launch_yang)
        tv_page.verify_text_in_tv_page()