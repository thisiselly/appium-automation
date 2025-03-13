from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.enums import WaitCondition
from utils.logs_util import logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def find_element(self, locator, wait_condition=WaitCondition.PRESENCE, retry=3, timeout=10):
        """
        find the element
        :param locator: the locator
        :param wait_condition: The wait condition to use (default is WaitCondition.PRESENCE)
        :param retry: retry times
        :param timeout: timeout seconds
        :return: return the element
        """
        attempts = 1
        while attempts <= retry:
            try:
                logger.info(f"finding element: {locator}")
                if wait_condition == WaitCondition.PRESENCE:
                    condition = EC.presence_of_element_located(locator)
                elif wait_condition == WaitCondition.CLICKABLE:
                    condition = EC.element_to_be_clickable(locator)
                elif wait_condition == WaitCondition.VISIBLE:
                    condition = EC.visibility_of_element_located(locator)
                elif wait_condition == WaitCondition.SELECTED:
                    condition = EC.element_to_be_selected(locator)
                elif wait_condition == WaitCondition.INVISIBLE:
                    condition = EC.invisibility_of_element_located(locator)
                else:
                    raise ValueError(f"Unsupported wait condition: {wait_condition}")

                ele = WebDriverWait(self.driver, timeout).until(condition)
                logger.info(f"element {locator} found")
                return ele

            except (TimeoutException, NoSuchElementException) as e:
                logger.error(f"element {locator} not found, retrying {attempts} time(s), exception msg: {str(e)}")
                attempts += 1

        raise TimeoutException(f"element {locator} not found after {retry} attempt(s).")

    def find_elements(self, locator, wait_condition=WaitCondition.PRESENCE_ALL, retry=3, timeout=10):
        """
        find the elements
        :param locator: the locator
        :param wait_condition: The wait condition to use (default is WaitCondition.ALL_ELEMENTS_PRESENCE)
        :param retry: retry times
        :param timeout: timeout seconds
        :return: returns the list of elements
        """
        attempts = 1
        while attempts <= retry:
            try:
                logger.info(f"finding elements: {locator}")
                if wait_condition == WaitCondition.PRESENCE_ALL:
                    condition = EC.presence_of_all_elements_located(locator)
                elif wait_condition == WaitCondition.VISIBLE_ALL:
                    condition = EC.visibility_of_all_elements_located(locator)
                else:
                    raise ValueError(f"Unsupported wait condition: {wait_condition}")

                all_ele = WebDriverWait(self.driver, timeout).until(condition)
                logger.info(f"elements {locator} found")
                return all_ele
            except (TimeoutException, NoSuchElementException) as e:
                logger.error(f"elements {locator} not found, retrying {attempts} time(s), exception: {str(e)}")
                attempts += 1

        raise TimeoutException(f"elements {locator} not found after {retry} attempt(s).")

    def clear(self, locator):
        """
        clear the input window
        :param locator: the locator
        :return: None
        """
        ele = self.find_element(locator)
        ele.clear()

    def send_keys(self, locator, content):
        """
        send keys in the input window
        :param locator: the locator
        :param content: the input content
        :return: None
        """
        ele = self.find_element(locator)
        ele.send_keys(content)

    def element_exist(self, locator, retry=3, timeout=10):
        """
        check the element exist or not
        :param locator: the locator
        :param retry: retry times
        :param timeout: timeout seconds
        :return: boolean value
        """
        try:
            logger.info(f"checking element {locator} exist or not")
            self.find_element(locator, retry=retry, timeout=timeout)
            logger.info(f"element {locator} exist")
            return True  # element found
        except (NoSuchElementException, TimeoutException):
            logger.info(f"element {locator} not found")
            return False  # element not found

    def click(self, locator):
        """
        click on the specific locator
        :param locator: the locator
        :return: None
        """
        logger.info(f"click element {locator}")
        ele = self.find_element(locator, wait_condition=WaitCondition.CLICKABLE)
        ele.click()

    def move_mouse_to_element(self, locator):
        """
        move the mouse to the element
        :param locator: the locator
        :return: None
        """
        logger.info(f"move the mouse to element {locator}")
        ele = self.find_element(locator)
        self.actions.move_to_element(ele).perform()

    # def move_mouse_by_coordinates(self, x, y):
    #     """
    #     move the mouse from x to y
    #     :param x:
    #     :param y:
    #     :return:
    #     """
    #     self.actions.move_by_offset(x, y).perform()

    def get_text(self, locator):
        """
        get the locator's text
        :param locator: the locator
        :return: the text value
        """
        ele = self.find_element(locator)
        if ele.text is not None:
            logger.info(f"get text from text: {ele.text}")
            return ele.text
        elif ele.accessible_name is not None:
            logger.info(f"get text from accessible_name: {ele.accessible_name}")
            return ele.accessible_name
        else:
            logger.info(f"text and accessible_name is none")
            return None

    def back(self, times=1):
        for _ in range(times):
            self.driver.back()
