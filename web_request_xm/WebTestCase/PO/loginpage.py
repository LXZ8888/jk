'''
管理登录页面所有的元素对象:(管理元素定位方式+定位的值+元素操作方法)
扩展：业务关键字

'''
from until.browser import   Browser
from selenium.webdriver.common.by import By
class LoginPage(Browser):
    username=(By.NAME,'accounts') #元祖
    pwd=(By.NAME,'pwd')
    loginButton=(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button')


    def type_unsername(self,value):
        '''用户名输入方法'''

        self.find_element(LoginPage.username).send_keys(value)  # 1.输入用户名

    def type_password(self,value):
        self.find_element(LoginPage.pwd).send_keys(value)  # 1.输入密码

    def type_login_button(self):
        self.find_element(LoginPage.loginButton).click()  # 1.点击登录按钮


    def login(self,username,password):
        '''登录的业务关键字'''
        self.type_unsername(username)
        self.type_password(password)
        self.type_login_button()