import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests
import logging


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

browser = testdata['browser']


@pytest.fixture(scope="session")
def brows():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    # driver.implicitly_wait(testdata['wait'])
    # driver.maximize_window()
    # driver.get(address)
    # time.sleep(testdata['sleep_time'])
    yield driver
    driver.quit()


@pytest.fixture()
def login():
    try:
        res1 = requests.post(testdata['address'] + '/gateway/login', data = {'username': testdata['username'], 'password': testdata['password']})
    except:
        logging.exception('Invalid credentials, no token')
        return None
    return res1.json()["token"]


@pytest.fixture()
def testtext1():
    return 'Title'


@pytest.fixture()
def good_word():
    return 'Привет'


@pytest.fixture()
def bad_word():
    return 'Првет'