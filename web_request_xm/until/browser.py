from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Browser():
    '''
    浏览器基础类：封装了浏览常用操作方法
    封装等待时间方法
    日志打印方法，
    错误截图方法
    '''

    def __init__(self,driver):
        self.driver=driver
        self.driver.get('http://42.192.6.197/?s=user/logininfo.html')

    def find_element(self,loc):
        '''找元素方法
        返回的是元素对象
        '''
        return self.driver.find_element(*loc)

    def _click(self,loc):
        '''点击方法
        点击之前自动加上显式等待时间'''
        self.wait_element_visible(loc).click()
    def _send_keys(self,loc,value):
        '''输入方法
             输入之前自动加上显式等待时间'''
        self.wait_element_visible(loc).send_keys(value)

    def wait_element_visible(self,loc):
        '''等待元素出现，找到元素
        返回的是元素对象
        '''
        #print('自动化显式等待元素中...')
        ele=WebDriverWait(self.driver,6).until(EC.visibility_of_element_located(loc))
        return ele