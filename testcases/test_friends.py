from pages.page_friends import FriendsPage


class TestFriends:

    def test_switch_to_friends_tab(self, launch_app):
        friend_page = FriendsPage(launch_app)
        friend_page.verify_text_in_friend_page()