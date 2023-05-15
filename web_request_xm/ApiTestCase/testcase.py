import json

import requests
import unittest
from ddt import ddt,data,unpack,file_data
'''
-表示一个用例
'''
'''假设性原则：所有的用例都需要加上auth认证
        所有的用例都需要加上token
        
'''
from until.logs import logger
from until.RW_excel import get_case
caseDatas=get_case()    #所有用例的数据,(1,[1])
caseDatas=get_case((1,[1,3,2]))

# users=[
#     ('admin','123456'),
#     ('admin','123456xxx'),
#     ('adminxxx', '123456xxx'),
# ] #接口自动化的数据，来源于yaml文件/或者一个excel文件
from until.HttpRequest import HttpRequest
@ddt #1代表这个类里面的测试用例需要用到ddt数据驱动
class Test(unittest.TestCase):
    INDEX=0  #类变量
    '''测试用例类：本地服务接口项目'''
    @classmethod
    def setUpClass(self) -> None:

        self.s=HttpRequest()

    @data(*caseDatas)
    #@file_data(r'../config/apiData.yaml')
    def testcase(self,caseData): #3定义变量接收数据
        #print(caseData)
        Test.INDEX+=1
        apiName=caseData[0] #接口名称
        args=caseData[2]  #接口参数
        method=caseData[1] #方法
        rheaders=caseData[5]  #请求类型
        tiqu=caseData[6] #变量提取
        url_pre=caseData[7]  #接口前缀
        url_path=url_pre+apiName
        validate=caseData[3]
        #print('开始运行第{}个用例'.format(Test.INDEX))
        logger.info('开始运行第{}个用例'.format(Test.INDEX))
        res=self.s.sendRequest(url_path=url_path,
                               method=method,
                               args=args,
                               rheaders=rheaders,
                               tiqu=tiqu,
                               v=validate)
        #print(res)
        #print('断言结果',res[1])
        logger.info('第{}个用例的断言结果为{}'.format(Test.INDEX,res[1]))

        #self.assertTrue(res[1])
        '''F 断言失败.  E（代码报错）'''
    '''
        新增其它接口的测试用例：新增yaml文件，新增用例方法：
        一个项目，所有的接口自动化用例，都只用到一个函数
        1.把接口的入参 参数化
        2.接口的名称（login），接口的请求方式，断言等等 参数化
    '''

    '''用户的新增接口:新增yaml文件，'''
    # @file_data(r'../config/apiData.yaml')
    # def test_add(self):
    #     url ='http://127.0.0.1:7001/api/qingfeng/users'
    #     res=self.s.request(url=url,method='get',json=users)
    #     # print(res.json())

if __name__ == '__main__':
    unittest.main()

