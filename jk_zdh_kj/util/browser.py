
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Browser():

    def __init__(self,driver):
        self.driver=driver
        self.driver.get('http://42.192.6.197:8082/?s=user/loginInfo.html')

    def find_element(self,loc):

        return self.driver.find_element(*loc)

    def _click(self,loc):
        '''�������
        ���֮ǰ�Զ�������ʽ�ȴ�ʱ��'''
        self.wait_element_visible(loc).click()
    def _send_keys(self,loc,value):
        '''���뷽��
             ����֮ǰ�Զ�������ʽ�ȴ�ʱ��'''
        self.wait_element_visible(loc).send_keys(value)

    def wait_element_visible(self,loc):
        '''�ȴ�Ԫ�س��֣��ҵ�Ԫ��
        ���ص���Ԫ�ض���
        '''
        #print('�Զ�����ʽ�ȴ�Ԫ����...')
        ele=WebDriverWait(self.driver,6).\
            until(EC.visibility_of_element_located(loc))
        return ele