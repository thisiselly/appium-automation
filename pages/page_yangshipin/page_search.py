from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import BasePage
from utils.assert_util import *


class SearchPage(BasePage):
    # search elements
    search_window = (AppiumBy.ID, "search_tv")
    search_input = (AppiumBy.ID, "search_input")
    search_button = (AppiumBy.ID, "search_tv")
    search_result_text = (AppiumBy.ID, "first_line")
    search_result_poster = (AppiumBy.ID, "poster")

    def select_search_after_input(self):
        self.click(self.search_button)

    def input_search_string(self, search_string):
        self.click(self.search_window)
        self.send_keys(self.search_input, search_string)

    def search_for_content(self, search_string):
        self.input_search_string(search_string)
        self.select_search_after_input()

    def get_all_search_title(self):
        all_ele = self.find_elements(self.search_result_text)
        all_displayed_text = []
        for ele in all_ele:
            all_displayed_text.append(ele.text)
        return all_displayed_text

    def get_all_search_posters(self):
        return self.find_elements(self.search_result_poster)

    def verify_search_result(self, search_string):
        all_displayed_text = self.get_all_search_title()
        result =  all(search_string.lower() in x.lower() for x in all_displayed_text)
        assert_true(result, f"not all displayed result contains search string {search_string}")

    def select_search_poster(self, from_index=0):
        all_posters = self.get_all_search_posters()
        all_posters[from_index].click()

