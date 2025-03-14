
import pytest

from pages.page_calculator.page_calculator import PageCalculator
from utils.get_file_path_util import get_csv_file_path
from utils.read_files import read_csv_file


class TestCaculator:
    calc_csv_path = get_csv_file_path() + r"\testdata_calculator.csv"

    @pytest.mark.parametrize("first_num, method, second_num, expect_result", read_csv_file(calc_csv_path))
    def test_cal_basic(self, launch_calc, first_num, method, second_num, expect_result):
        page_calc = PageCalculator(launch_calc)
        page_calc.verify_basic_function_of_calc(first_num, method, second_num, expect_result)
    #
    @pytest.mark.p1
    def test_pai(self, launch_calc):
        page_calc = PageCalculator(launch_calc)
        page_calc.verify_pai()

    @pytest.mark.p1
    def test_factorial(self, launch_calc):
        page_calc = PageCalculator(launch_calc)
        page_calc.verify_factorial()