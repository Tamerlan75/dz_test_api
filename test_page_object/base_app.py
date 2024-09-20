import logging
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# from selenium import webdriver
# from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://test-stand.gb.ru'

    def find_element(self, locator, time=3):
        # if mode == 'css':
        #     element = self.driver.find_element(By.CSS_SELECTOR, path)
        # if mode == 'xpath':
        #     element = self.driver.find_element(By.XPATH, path)
        # else:
        #     element = None
        #
        # return element
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'can not fined element by locator')
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f'Property {property} not found in element with locator {locator}')
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exeption while open site')
            start_browsing = None
        return start_browsing

    def alert_text(self):
        time.sleep(3)
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception('Exception find alert')
            return None


