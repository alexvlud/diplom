import os, pickle
from SmartPageObject.pages.base import WebPage
from SmartPageObject.pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)


    username = WebElement(id='username')
    password = WebElement(id='password')

    btn = WebElement(id='kc-login')
    lk = WebElement(id='lk-btn')

    # Auth block - Phone
    auth_phone = WebElement(id='t-btn-tab-phone')

    auth_mail = WebElement(id='t-btn-tab-mail')

    auth_login = WebElement(id='t-btn-tab-login')

    auth_ls = WebElement(id='t-btn-tab-ls')







