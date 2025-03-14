# import time
#
# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# import pytest
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class TestTasks:
#     new_task = (AppiumBy.ID, "new_event_fab")
#     task_subject = (AppiumBy.ID, "edit_fragment_subject")
#     due_date = (AppiumBy.ID, "edit_fragment_due_date")
#
#
#     def test_add_task(self,open_app):
#         driver = open_app
#         new_task_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located(self.new_task))
#         new_task_button.click()
#         task_subject_element = WebDriverWait(driver,10).until(EC.visibility_of_element_located(self.task_subject))
#         task_subject_element.send_keys("HY Task")
#         task_subject_element = WebDriverWait(driver,10).until(EC.visibility_of_element_located(self.due_date))
#         task_subject_element.click()
#         time.sleep(1)
#
#         # click on the month button
#         select_list = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.Spinner')
#         time.sleep(1)
#         select_list[0].click()
#
#         #select month
#         get_month = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("May")')
#         get_month.click()
#         #select month
#
#         # click on the year button
#         select_list[1].click()
#
#         # get year
#         get_year = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("2027")')
#         get_year.click()
#
#         # get_date = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'index("15")')
#         # get_date = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'text("15")')
#         # get_date.click()
#
#         target_date_content_desc = "Saturday, May 15, 2027"
#         date_element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, target_date_content_desc))
#         )
#         # 当有content_desc 时，可以用accessbility
#         date_element.click()
#
#         driver.find_element(AppiumBy.ID, 'button1').click()
#
#         select_repeat = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.Spinner')
#         select_repeat[0].click()
#
#
#
