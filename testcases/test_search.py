from pages.page_search import SearchPage


class TestSearch:
    def test_search_movie(self, launch_app):
        search_string = "supersimplesongs"
        search_page = SearchPage(launch_app)
        search_page.search_for_content(search_string)
        search_page.verify_search_result(search_string)
