'''
�����¼ҳ�����е�Ԫ�ض���:(����Ԫ�ض�λ��ʽ+��λ��ֵ+Ԫ�ز�������)
��չ��ҵ��ؼ���

'''
from util.browser import   Browser
from selenium.webdriver.common.by import By
class LoginPage(Browser):
    username=(By.NAME,'accounts') #Ԫ��
    pwd=(By.NAME,'pwd')
    loginButton=(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button')


    def type_unsername(self,value):
        '''�û������뷽��'''

        self.find_element(LoginPage.username).send_keys(value)  # 1.�����û���

    def type_password(self,value):
        self.find_element(LoginPage.pwd).send_keys(value)  # 1.��������

    def type_login_button(self):
        self.find_element(LoginPage.loginButton).click()  # 1.�����¼��ť


    def login(self,username,password):
        '''��¼��ҵ��ؼ���'''
        self.type_unsername(username)
        self.type_password(password)
        self.type_login_button()