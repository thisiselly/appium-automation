import time

from pages.page_home import HomePage


class TestHome:
    def test_on_home_page_default(self, launch_app):
        home_page = HomePage(launch_app)
        home_page.go_to_home_tab()
        home_page.verify_text_in_home_page()


    def test_switch_to_live_tab(self, launch_app):
        home_page = HomePage(launch_app)
        home_page.go_to_live_tab()
        home_page.verify_text_in_live_page()

    def test_switch_to_friend_tab(self, launch_app):
        home_page = HomePage(launch_app)
        home_page.go_to_friend_tab()
        home_page.verify_text_in_friend_page()

    def test_switch_to_me_tab(self, launch_app):
        home_page = HomePage(launch_app)
        home_page.go_to_me_tab()
        home_page.verify_text_in_me_page()

