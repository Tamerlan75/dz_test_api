from base_app import BasePage
from selenium.webdriver.common.by import By
from zeep import Client, Settings
import time
import logging
import yaml
import requests

class TestSearchLocators:
    # LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    # LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    # LOCATOR_BTN_LOGIN = (By.XPATH, '//*[@id="login"]/div[3]/button')
    # LOCATOR_HELLO_LOGIN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')
    # LOCATOR_BTN_CREATE_POST = (By.XPATH, '//*[@id="create-btn"]')
    # LOCATOR_TITLE_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    # LOCATOR_DESCRIPTION_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    # LOCATOR_CONTENT_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    # LOCATOR_SAVE_POST = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button')
    # LOCATOR_TEST_TITLE = (By.XPATH, '/html/body/div[1]/main/div/div[1]/h1')
    # LOCATOR_BTN_CONTACT = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')
    # LOCATOR_NAME_FIELD = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    # LOCATOR_EMAIL_FIELD = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    # LOCATOR_CONTENT2_FIELD = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    # LOCATOR_BTN_CONT_US = (By.XPATH, '//*[@id="contact"]/div[4]/button')
    ids = dict()
    with open('testdata.yaml') as f:
        locators = yaml.safe_load(f)
        #testdata = yaml.safe_load(f)

    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])


class OperationsHelper(BasePage):

    with open('testdata.yaml') as f:
        testdata = yaml.safe_load(f)

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exeption while operation with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exeptiom with click')
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text


#ENTER_TEXT
    def enter_login(self, word):
        # logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]})
        # login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        # login_field.clear()
        # login_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login form')


    def enter_pass(self, word):
        # logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]})
        # login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        # login_field.clear()
        # login_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='Pass form')

    def enter_title(self, word):
    # logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_TITLE_FIELD[1]}')
    # title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_FIELD)
    # title_field.clear()
    # title_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_TITLE_FIELD'], word, description='Title form')

    def enter_description(self, word):
        # logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION_FIELD[1]}')
        # description_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_FIELD)
        # description_field.clear()
        # description_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_DESCRIPTION_FIELD'], word, description='Description form')

    def enter_content(self, word):
        # logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}')
        # content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        # content_field.clear()
        # content_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_FIELD'], word, description='Content form')

    def enter_name(self, word):
        # logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}')
        # name_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        # name_field.clear()
        # name_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_NAME_FIELD'], word, description='Name form')

    def enter_email(self, word):
        # logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_EMAIL_FIELD[1]}')
        # email_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        # email_field.clear()
        # email_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_EMAIL_FIELD'], word, description='Email form')

    def enter_content2(self, word):
        # logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_CONTENT2_FIELD[1]}')
        # content2_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT2_FIELD)
        # content2_field.clear()
        # content2_field.send_keys(word)
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT2_FIELD'], word, description='Content2 form')

#CLICK_BUTTON
    def click_button_login(self):
        # logging.info('Click button login')
        # self.find_element(TestSearchLocators.LOCATOR_BTN_LOGIN).click()
        self.click_button(TestSearchLocators.ids['LOCATOR_BTN_LOGIN'], description='login')

    def click_button_create_post(self):
        time.sleep(3)
        # logging.info('Click button create post')
        # self.find_element(TestSearchLocators.LOCATOR_BTN_CREATE_POST).click()
        self.click_button(TestSearchLocators.ids['LOCATOR_BTN_CREATE_POST'], description='Button create post')

    def click_button_save_post(self):
        # logging.info('Click button save post')
        # self.find_element(TestSearchLocators.LOCATOR_SAVE_POST).click()
        self.click_button(TestSearchLocators.ids['LOCATOR_SAVE_POST'], description='Button save post')

    def click_button_contact(self):
        # logging.info('Click on the contact button to enter the name')
        # self.find_element(TestSearchLocators.LOCATOR_BTN_CONTACT).click()
        self.click_button(TestSearchLocators.ids['LOCATOR_BTN_CONTACT'], description='Button contact')

    def click_button_cont_us(self):
        # logging.info('Click on the cont_us button to enter information')
        # self.find_element(TestSearchLocators.LOCATOR_BTN_CONT_US).click()
        self.click_button(TestSearchLocators.ids['LOCATOR_BTN_CONT_US'], description='Button cont_us')

#GET TEXT
    def get_hello_text(self):
        # hello_field = self.find_element(TestSearchLocators.LOCATOR_HELLO_LOGIN, time=3)
        # text = hello_field.text
        # logging.info(f'We find text {text} in field {TestSearchLocators.LOCATOR_HELLO_LOGIN[1]}')
        # return hello_field.text
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_HELLO_LOGIN'], description='Hello login')

    def get_title_text(self):
        time.sleep(3)
        # title = self.find_element(TestSearchLocators.LOCATOR_TEST_TITLE, time=3)
        # text = title.text
        # logging.info(f'We find text {text} in field {TestSearchLocators.LOCATOR_TEST_TITLE[1]},'
        #              f' to check the creation of the post')
        # return text
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_TEST_TITLE'], description='Title')
#ALERT
    def alert(self):

        # alert = self.driver.switch_to.alert
        # text = alert.text
        text = self.alert_text()
        logging.info(f'We find text {text} in field alert,'
                     f' to check the output of the alert')
        return text

    def receiving_posts_another_rest_api(self, login):
        header = {'X-Auth-Token': login}
        try:
            res = requests.get(self.testdata['address'] + "/api/posts", params={'owner': 'notMe'}, headers=header)
            listres = [i['title'] for i in res.json()['data']]
        except:
            logging.exception(f'Failed to make a request for {self.testdata['address'] + "/api/posts"}')
            return None
        logging.info("We received a list of another user's posts")
        return listres

    def checkText(self, text):
        wsdl = self.testdata['wsdl']
        settings = Settings(strict=False)
        client = Client(wsdl=wsdl, settings=settings)
        result = client.service.checkText(text)
        if not result:
            logging.error('Failed to get the words')
        logging.debug('Got the right words')
        return result[0]['s']

    def post(self, login):
        header = {'X-Auth-Token': login}
        res1 = requests.post(self.testdata['address'] + "/api/posts",
                             data={'title': self.testdata['title'], 'description': self.testdata['description'],
                                   'content': self.testdata['content']}, headers=header)
        return res1.json()

    def receiving_posts_user_rest_api(self, login):
        header = {'X-Auth-Token': login}
        try:
            res2 = requests.get(self.testdata['address'] + "/api/posts", headers=header)
            listres1 = [i['description'] for i in res2.json()['data']]
        except:
            logging.exception(f'Failed to make a request for {self.testdata['address'] + "/api/posts"}')
            return None
        logging.info("We received a list of another user's posts")
        return listres1





