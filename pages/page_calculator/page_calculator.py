import random as random

from appium.webdriver.common.appiumby import AppiumBy
import time
from base.base_page import BasePage
from utils.assert_util import *


def calculate_factorial(nums):
    if nums == 0:
        return 1
    if nums == 1:
        return 1
    else:
        return nums * calculate_factorial(nums - 1)

class PageCalculator(BasePage):
    # elements
    result_preview = (AppiumBy.ID, "result_preview")
    result_final = (AppiumBy.ID, "result_final")
    clear_button = (AppiumBy.ID, "clr")
    equals = (AppiumBy.ID, 'eq')
    pai = (AppiumBy.ID, 'const_pi')
    factorial = (AppiumBy.ID, 'op_fact')
    expect_error_msg = "Can't divide by 0"

    calc_dict = {
        "1": "digit_1",
        "2": "digit_2",
        "3": "digit_3",
        "4": "digit_4",
        "5": "digit_5",
        "6": "digit_6",
        "7": "digit_7",
        "8": "digit_8",
        "9": "digit_9",
        "0": "digit_0",
        '=': "eq",
        '+': "op_add",
        '-': "op_sub",
        '*': "op_mul",
        '/': "op_div",
        '.': "dec_point",
        '^': "op_pow"
    }

    def click_number(self, nums):
        for char in str(nums):
            single_char = self.calc_dict[str(char)]
            locator = (AppiumBy.ID, single_char)
            self.click(locator)

    def clear_input(self):
        self.click(self.clear_button)

    def get_final_result(self):
        return self.get_text(self.result_final)

    def get_result_preview(self):
        return self.get_text(self.result_preview)

    def verify_basic_function_of_calc(self, first_num, method, second_num, expect_result):
        self.clear_input()

        # input the first num
        self.click_number(first_num)

        # click the method
        locator = (AppiumBy.ID, self.calc_dict[method])
        self.click(locator)

        # input the second method
        self.click_number(second_num)

        # click equal button
        self.click(self.equals)

        if expect_result != "Error":
            actual_result = self.get_final_result().replace('−', '-')
            assert_equal(str(expect_result), str(actual_result), "error msg incorrect")
        else:
            actual_error_text = self.get_result_preview()
            assert_equal(self.expect_error_msg, actual_error_text, "result incorrect")

    def verify_pai(self):
        self.clear_input()
        self.click(self.pai)
        actual_result = self.get_result_preview()
        assert_equal("3.1415926535897", actual_result, "incorrect")

    def verify_factorial(self):
        self.clear_input()
        n = random.randint(0, 15)
        expect_result = str(calculate_factorial(n))
        self.click_number(n)
        self.click(self.factorial)
        self.click(self.equals)
        actual_result = self.get_final_result()
        assert_equal(expect_result, actual_result, "calculate fail")
