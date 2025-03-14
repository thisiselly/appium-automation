from pages.page_yangshipin.page_my_profile import MyProfilePage
from pages.page_yangshipin.page_play import PlayPage
from pages.page_yangshipin.page_search import SearchPage


class TestMyProfile:

    def test_switch_to_my_profile_tab(self, launch_yang):
        my_profile_page = MyProfilePage(launch_yang)
        my_profile_page.verify_text_in_my_profile_page()

    def test_add_video_in_collection(self, launch_yang):
        search_string = "supersimplesongs"
        search_page = SearchPage(launch_yang)
        search_page.search_for_content(search_string)
        search_page.select_search_poster()
        play_page = PlayPage(launch_yang)
        play_page.select_fav_button()
        video_title = play_page.get_play_video_title()
        play_page.back(2)
        my_profile_page = MyProfilePage(launch_yang)
        my_profile_page.go_to_my_collection()
        my_profile_page.verify_collection_list(video_title, exist=True)

    def test_remove_video_in_collection(self, launch_yang):
        my_profile_page = MyProfilePage(launch_yang)
        my_profile_page.go_to_my_collection()
        my_profile_page.select_first_video_in_collection()
        play_page = PlayPage(launch_yang)
        play_page.select_fav_button()
        video_title = play_page.get_play_video_title()
        play_page.back(2)
        my_profile_page.go_to_my_collection()
        my_profile_page.verify_collection_list(video_title, exist=False)
