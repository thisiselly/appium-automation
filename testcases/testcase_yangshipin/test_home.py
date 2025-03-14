from pages.page_yangshipin.page_home import HomePage


class TestHome:
    def test_on_home_page_default(self, launch_yang):
        home_page = HomePage(launch_yang)
        home_page.go_to_home_tab()
        home_page.verify_text_in_home_page()
