import requests
import unittest
from ddt import ddt,data,unpack

'''数据驱动，具体步骤看思维导图，案例就是登录'''

'''假设性原则：所有的用例都需要加上auth认证
        所有的用例都需要加上token
'''

users=[
    ('admin','123456'),
    ('admin','123456xxx'),
    ('adminxxx', '123456xxx'),
] #接口自动化的数据，来源于yaml文件，或者一个excel文件

@ddt #1代表这个类里面的测试用例需要用到ddt数据驱动
class Test(unittest.TestCase):
    '''测试用例类：本地服务接口项目'''
    @classmethod
    def setUpClass(self) -> None:
        '''所有用例的前置操作：创建一个会话，统一设置headers参数'''
        self.s=requests.session()
        self.s.auth = ('admin', '123456')
        self.s.headers.update({"Token":"qingfengtest"})



    @unpack
    @data(*users)
    def test04(self,username,pwd): #3定义变量接收数据
        '''登录用例:正确的用户名和密码'''
        print(username,pwd)
        def test01(self):
            '''测试用例1'''
            url_text='http://127.0.0.1:7001/api/qingfeng/text'
            d='qingfengtest'
            #res=requests.request(method='post',url=url_text,data=d)
            res=self.s.request(method='post',url=url_text,data=d)
            print(res.request.headers)
            respone=res.json() #{'code': '000', 'data': 'qingfengtest'}
        #     '''断言'''
        #     self.assertEqual(res.status_code,200) #实际结果，是否等于预期结果
        #     self.assertEqual(respone['code'],'000')
        #
        #
        # def test02(self):
        #     url_json='http://127.0.0.1:7001/api/qingfeng/user'
        #     d={
        #         "username":"qingfeng",
        #         "phone":123455667
        #     } #字典
        #     res=self.s.request(method='post',url=url_json,json=d)
        #     print(res.request.headers)
        #
        #     print(res.status_code)
        #     print(res.json())
        #
        #
        # def test03(self):
        #     url_auth = 'http://127.0.0.1:7001/api/qingfeng/auth'
        #     d = {
        #         "id": 123456789
        #     }
        #     res = self.s.request(method='post', url=url_auth, json=d)
        #     print(res.request.headers)
        #
        #     print(res.json())

        # @data('admin','adminxxx') #2.作为参数化的数据,逗号隔开的代表一个用例，
        # @data(('admin', '123456','111'), ('adminxxx', '123456xxx','111'))
        # @unpack

        '''
                users=[
                ('admin','123456'),
                ('admin','123456xxx'),
                ('adminxxx', '123456xxx'),
            ] 
        '''

        # url_login='http://127.0.0.1:7001/api/qingfeng/login'
        # users={
        #     'username':username,
        #     'password':pwd
        # }
        # res=self.s.request(url=url_login,method='post',json=users)
        # print(res.json())

    # def test05(self):
    #     '''登录用例:错误的用户名和密码'''
    #     url_login='http://127.0.0.1:7001/api/qingfeng/login'
    #     users={
    #         'username':"adminxxxx",
    #         'password':"123456xxx"
    #     }
    #     res=self.s.request(url=url_login,method='post',json=users)
    #     print(res.json())
# class Test1(unittest.TestCase):
#     '''测试用例类：论坛项目接口测试项目'''

# class Test2(unittest.TestCase):
#     '''测试用例类：电商项目接口测试项目'''

if __name__ == '__main__':
    unittest.main(verbosity=2)


'''作业：python+request+unittest+htmltestrunner+ddt(数据驱动)
论坛项目接口

数据驱动：关键字驱动
'''