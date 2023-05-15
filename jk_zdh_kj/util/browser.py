
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Browser():

    def __init__(self,driver):
        self.driver=driver
        self.driver.get('http://42.192.6.197:8082/?s=user/loginInfo.html')

    def find_element(self,loc):

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
        ele=WebDriverWait(self.driver,6).\
            until(EC.visibility_of_element_located(loc))
        return ele