from pages.page_yangshipin.page_friends import FriendsPage


class TestFriends:

    def test_switch_to_friends_tab(self, launch_yang):
        friend_page = FriendsPage(launch_yang)
        friend_page.verify_text_in_friend_page()

    def test_swipe_to_diff_tabs(self, launch_yang):
        friend_page = FriendsPage(launch_yang)
        friend_page.verify_swipe_to_diff_tabs()