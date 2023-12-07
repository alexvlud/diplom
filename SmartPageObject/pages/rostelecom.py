#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from SmartPageObject.pages.base import WebPage
from SmartPageObject.pages.elements import WebElement
from SmartPageObject.pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    # Footer agreements
    footer_agreements = WebElement(id='rt-footer-agreement-link')

    # Footer cookies tip
    footer_cookies = WebElement(id='cookies-tip-open')
    footer_cookies_tip = WebElement(css_selector='div.rt-tooltip.rt-tooltip--rounded.rt-tooltip--topLeft.rt-cookies-tip')


    #Auth block - Phone
    auth_phone = WebElement(id='t-btn-tab-phone')
    auth_phone_checked = WebElement(css_selector='div#t-btn-tab-phone.rt-tab.rt-tab--small.rt-tab--active')

    # Auth block - mail
    auth_mail = WebElement(id='t-btn-tab-mail')

    # Auth block - login
    auth_login = WebElement(id='t-btn-tab-login')

    # Auth block - personal account
    auth_ls = WebElement(id='t-btn-tab-ls')

    #Auth block - input placeholder
    input_placeholder = WebElement(css_selector='span.rt-input__placeholder')



    # Auth block - Help
#    auth_help = WebElement(id='cookies-tip-open')

    # Auth block - registration
    auth_registration = WebElement(id='kc-register')

    #Auth block - agreements
    auth_agreements = WebElement(id='rt-auth-agreement-link')

    #Auth block - VK
    auth_vk = WebElement(id='oidc_vk')

    # Auth block - OK
    auth_ok = WebElement(id='oidc_ok')

    # Auth block - mail.ru
    auth_mail_ru = WebElement(id='oidc_mail')

    # Auth block - Ya
    auth_ya = WebElement(id='oidc_ya')

    # Auth block - forgot password
    auth_forgot = WebElement(id='forgot_password')

    # Skype call
    skype_call = WebElement(xpath='//*[@id="app-footer"]/div[2]/a[1]')

    #Check box remember me is checked
    remember_me_is_checked = WebElement(css_selector='div.rt-checkbox.rt-checkbox--checked')

    # Check box remember me is unchecked
    remember_me_is_unchecked = WebElement(css_selector='div.rt-checkbox')




'''
    # Main search field
    search = WebElement(id='header-search')

    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')
'''