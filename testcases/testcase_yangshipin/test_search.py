from pages.page_yangshipin.page_search import SearchPage


class TestSearch:
    def test_search_movie(self, launch_yang):
        search_string = "supersimplesongs"
        search_page = SearchPage(launch_yang)
        search_page.search_for_content(search_string)
        search_page.verify_search_result(search_string)
