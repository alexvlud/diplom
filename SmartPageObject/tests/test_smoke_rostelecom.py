#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#

import pytest
import time
from SmartPageObject.pages.rostelecom import MainPage


# def test_check_main_search(web_browser):
#    """ Make sure main search works fine. """

#    page = MainPage(web_browser)

@pytest.mark.skip(reason="#1-Ok")
def test_check_vk_auth(web_browser):
    page = MainPage(web_browser)

    page.auth_vk.click()

    assert page.get_current_url()[:22] == 'https://id.vk.com/auth'


@pytest.mark.skip(reason="#2-Ok")
def test_check_ok_auth(web_browser):
    page = MainPage(web_browser)

    page.auth_ok.click()

    assert page.get_current_url()[:24] == 'https://connect.ok.ru/dk'


@pytest.mark.skip(reason="#3-Ok")
def test_check_mail_ru_auth(web_browser):
    page = MainPage(web_browser)


    page.auth_mail_ru.click()

    assert page.get_current_url()[:39] == 'https://connect.mail.ru/oauth/authorize'


@pytest.mark.skip(reason="#4-Разобраться с яндексом и хромом. Долго грузится")
def test_check_ya_auth(web_browser):
    page = MainPage(web_browser)

    page.auth_ya.click()

    assert page.get_current_url()[:33] == 'https://oauth.yandex.ru/authorize'


@pytest.mark.skip(reason="#5-Ok")
def test_footer_cookies(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()

    page.footer_cookies.click()
    page.screenshot('cookies.png')

    assert page.footer_cookies_tip.find() != None


@pytest.mark.skip(reason="#6-Ok")
def test_footer_agreements_page(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()

    original_window = page.get_current_window_id()
    page.footer_agreements.click()
    time.sleep(1)
    page.switch_to_window(original_window)

    page.screenshot('footer_agreements.png')
    assert page.get_current_url() == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'


@pytest.mark.skip(reason="#7-Ok")
def test_registration_page(web_browser):
    page = MainPage(web_browser)

    page.auth_registration.click()

    assert page.get_current_url()[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'

@pytest.mark.skip(reason="#8-Alert")
def test_skype(web_browser):
    page = MainPage(web_browser)

    page.scroll_down()
    page.skype_call.click()
    page.wait_page_loaded()

    page.screenshot('skype.png')

@pytest.mark.skip(reason="#9-Ok")
def test_forgot_password_page(web_browser):
    page = MainPage(web_browser)

    page.auth_forgot.click()

    assert page.get_current_url()[:74] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'

@pytest.mark.skip(reason="#10- Ok")
def test_check_box_remember_me(web_browser):
    page = MainPage(web_browser)

    page.remember_me_is_checked.click()
    time.sleep(2)
    assert page.remember_me_is_unchecked.find()!=None

    page.remember_me_is_unchecked.click()
    time.sleep(2)
    assert page.remember_me_is_checked.find()!=None


@pytest.mark.skip(reason="#11- Ok")
def test_check_box_remember_me_checked_default(web_browser):
    page = MainPage(web_browser)

    assert page.remember_me_is_checked.find()!=None

@pytest.mark.skip(reason="#12- Ok")
def test_phone_checked_default(web_browser):
    page = MainPage(web_browser)

    assert page.auth_phone_checked.find() != None

@pytest.mark.skip(reason="#13- Ok")
def test_phone_checked_placeholder(web_browser):
    page = MainPage(web_browser)

    page.auth_phone.click()
    time.sleep(0.5)
    assert page.input_placeholder.get_text() == 'Мобильный телефон'


@pytest.mark.skip(reason="#14- Ok")
def test_mail_checked_placeholder(web_browser):
    page = MainPage(web_browser)

    page.auth_mail.click()
    time.sleep(0.5)
    assert page.input_placeholder.get_text() == 'Электронная почта'

@pytest.mark.skip(reason="#15- Ok")
def test_login_checked_placeholder(web_browser):
    page = MainPage(web_browser)

    page.auth_login.click()
    time.sleep(0.5)
    assert page.input_placeholder.get_text() == 'Логин'


@pytest.mark.skip(reason="#16- Ok")
def test_ls_checked_placeholder(web_browser):
    page = MainPage(web_browser)

    page.auth_ls.click()
    time.sleep(0.5)

    assert page.input_placeholder.get_text() == 'Лицевой счёт'


@pytest.mark.skip(reason="#17-Ok")
def test_auth_agreements_page(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()

    original_window = page.get_current_window_id()
    page.auth_agreements.click()
    time.sleep(1)
    page.switch_to_window(original_window)

    page.screenshot('auth_agreements.png')
    assert page.get_current_url() == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

