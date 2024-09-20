from testpage import OperationsHelper
import logging
import pytest
import time
import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

def test_step1(brows):
    logging.info('test_1 starting')
    testpage = OperationsHelper(brows)
    testpage.go_to_site()
    testpage.enter_login('testtest1')
    testpage.enter_pass('c23b2ed66e')
    testpage.click_button_login()
    assert testpage.get_hello_text() == 'Hello, testtest1'

def test_step2(brows):
    logging.info('test_2 starting')
    time.sleep(3)
    testpage = OperationsHelper(brows)
    testpage.click_button_create_post()
    time.sleep(2)
    testpage.enter_title('Заголовок')
    testpage.enter_description('Описание')
    testpage.enter_content('Контент')
    testpage.click_button_save_post()
    assert testpage.get_title_text() == 'Заголовок'

def test_step3(brows):
    logging.info('test_3 starting')
    testpage = OperationsHelper(brows)
    testpage.click_button_contact()
    testpage.enter_name('Timur')
    testpage.enter_email('t.mollaev7@yandex.ru')
    testpage.enter_content2('Какой-то контент')
    testpage.click_button_cont_us()
    assert testpage.alert() == 'Form successfully submitted'


def test_step4(testtext1, login):
    logging.info('test_4 starting')
    testpage = OperationsHelper(login)
    assert testtext1 in testpage.receiving_posts_another_rest_api(login)


def test_step5(good_word, bad_word):
    logging.info('test_5 starting')
    testpage = OperationsHelper(good_word)
    assert good_word in testpage.checkText(bad_word)


def test_step6(login):
    logging.info('test_6 starting')
    testpage = OperationsHelper(login)
    testpage.post(login)
    assert testdata['description'] in testpage.receiving_posts_user_rest_api(login)


fromaddr = "mollayev.tima@mail.ru"
toaddr = "mollayev.tima@mail.ru"
mypass = "zyNjfyAFGXNU8xP06PU0"
reportname = 'new.html'

msg = MIMEMultipart()
msg['from'] = fromaddr
msg['to'] = toaddr
msg['Subject'] = 'Привет'

with open(reportname, 'rb') as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = "attachment'; filename='%s'" % basename(reportname)
    msg.attach(part)
body = 'Тесты завершены'
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()










