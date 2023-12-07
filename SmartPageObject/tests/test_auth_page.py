import pytest,pickle,selenium
from SmartPageObject.pages.auth_page import AuthPage
import time
from SmartPageObject.pages.auth_data import phone, email, login, l_ack, password


@pytest.mark.parametrize('inp', [phone, email, login, l_ack])
def test_authorisation_from_phone_tab(web_browser, inp):

    page = AuthPage(web_browser)
    page.username.send_keys(inp)
    page.password.send_keys(password)

    page.btn.click()

    time.sleep(3)

    assert page.lk.find() != None

@pytest.mark.skip(reason="#13- Ok")
@pytest.mark.parametrize('inp', [phone, email, login, l_ack])
def test_authorisation_from_mail_tab(web_browser, inp):

    page = AuthPage(web_browser)
    page.auth_mail.click()
    page.username.send_keys(inp)
    page.password.send_keys(password)

    page.btn.click()

    time.sleep(3)

    assert page.lk.find() != None


@pytest.mark.skip(reason="#13- Ok")
@pytest.mark.parametrize('inp', [phone, email, login, l_ack])
def test_authorisation_from_login_tab(web_browser, inp):
    page = AuthPage(web_browser)
    page.auth_login.click()
    page.username.send_keys(inp)
    page.password.send_keys(password)

    page.btn.click()

    time.sleep(3)

    assert page.lk.find() != None


@pytest.mark.skip(reason="#13- Ok")
@pytest.mark.parametrize('inp', [phone, email, login, l_ack])
def test_authorisation_from_ls_tab(web_browser, inp):
    page = AuthPage(web_browser)
    page.auth_ls.click()
    page.username.send_keys(inp)
    page.password.send_keys(password)

    page.btn.click()

    time.sleep(3)

    assert page.lk.find() != None

