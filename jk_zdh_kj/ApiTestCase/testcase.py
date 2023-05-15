import json

import requests
import unittest
from util.RW_excel import get_case
from ddt import ddt, data, unpack, file_data
from util.HttpRequest import HttpRequest
from util.logs import logger


# E = ExcelWR(filePath=r'../config/jk-sj.xlsx')  # 路径
# caseDatas = E.readEx()

caseDatas = get_case()  # 所有用例的数据

'''假设性原则：所有的用例都需要加上auth认证
        所有的用例都需要加上token
'''


# users = [
#     ('admin', '123456'),
#     ('admin', '123456xxx'),
#     ('adminxxx', '123456xxx'),
# ]  # 接口自动化的数据，来源于yaml文件，或者一个excel文件


@ddt  # 1代表这个类里面的测试用例需要用到ddt数据驱动
class Test(unittest.TestCase):
    '''测试用例类：本地服务接口项目'''
    INDEX=0

    @classmethod
    def setUpClass(self) -> None:
        '''所有用例的前置操作：创建一个会话，统一设置headers参数'''
        self.s = HttpRequest()

    # def test01(self):
    #     '''测试用例1'''
    #     url_text = 'http://127.0.0.1:7001/api/qingfeng/text'
    #     d = 'qingfengtest'
    #     # res=requests.request(method='post',url=url_text,data=d)
    #     res = self.s.request(method='post', url=url_text, data=d)
    #     print('123', res.request.headers)
    #     respone = res.json()  # {'code': '000', 'data': 'qingfengtest'}
    #     '''断言'''
    #     self.assertEqual(res.status_code, 200)  # 实际结果，是否等于预期结果
    #     self.assertEqual(respone['code'], '000')

    # def test02(self):
    #     url_json = 'http://127.0.0.1:7001/api/qingfeng/user'
    #     d = {
    #         "username": "qingfeng",
    #         "phone": 123455667
    #     }  # 字典
    #     res = self.s.request(method='post', url=url_json, json=d)
    #     print('hhh', res.json())
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

    # @unpack
    # @data(*users)

    '''新增其他接口的测试用例：新增yaml文件，新增函数方法。一个项目所有的接口自动化用例，都只是用到一个函数
    1、把接口的入参 参数化
    2、把接口的名称（login） ,接口的请求方式，断言等，参数化
    '''

    @data(*caseDatas)
    # @file_data(r'D:\1967668484\git-资料测试总理-已提交\接口自动化\接口自动化框架\config\apiData.yaml')
    def testcase(self, caseData):  # 3定义变量接收数据
        Test.INDEX+=1
        print(Test.INDEX)
        '''登录用例:正确的用户名和密码'''
        # print(caseData)
        apiName = caseData[0]
        args = caseData[2]
        # if args:
        #     args = eval(args)
        # print(type(args), args)
        method = caseData[1]
        rt = caseData[5]
        tiqu = caseData[6]
        url_pre = caseData[7]
        url_path = url_pre + apiName
        validate=caseData[3]
        logger.info('开始运行第{}个用例'.format(Test.INDEX))

        res = self.s.sendRequest(url_path=url_path, method=method, args=args, rt=rt, tiqu=tiqu,v=validate)

        # print(res)
        self.assertTrue(res[1])



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
    unittest.main()
