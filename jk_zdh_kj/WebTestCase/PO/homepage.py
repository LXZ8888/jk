from selenium.webdriver.common.by import By

from util.browser import   Browser
'''��ҳԪ��po����'''
class HomePage():
    search_input=(By.ID,'search-input') #Ԫ��
    search_button=(By.ID,'ai-topsearch')

    def _search_input(self,browserInit,value):
        '''��ҳ������������������Ϊ�����Ĺؼ���'''
        #self.wait_element_visible(HomePage.search_input)
        #self.find_element(HomePage.search_input).send_keys(value)  # 1.�����û���
        browserInit._send_keys(HomePage.search_input,value)

    def _search_button(self,browserInit):
        '''������ť�ĵ��'''
        #self.wait_element_visible(HomePage.search_input)
        #self.find_element(HomePage.search_button).click()  # 1.�����¼��ť

        browserInit._click(HomePage.search_button)


    def search(self,browserInit,value):
        '''�����Ĺؼ���'''
        self._search_input(browserInit,value)
        self._search_button(browserInit)