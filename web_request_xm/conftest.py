'''
开始web自动化测试:
所有用例的前置操作：打开谷歌浏览器，url
'''
import time

from selenium import webdriver
import pytest
from until.browser import Browser
from WebTestCase.PO.loginpage import LoginPage
@pytest.fixture()
def browserInit():

    '''打开浏览器，登录'''
    driver=webdriver.Chrome()
    browser=Browser(driver)     #浏览器常用方法类是实例化对象
    return  browser

@pytest.fixture()
def browser_login(browserInit):
    time.sleep(5)
    browserInit._send_keys(LoginPage.username, 'admin1')
    browserInit._send_keys(LoginPage.pwd, 'shopxo')
    time.sleep(5)
    browserInit._click(LoginPage.loginButton)
    time.sleep(5)
    return browserInit


