'''所有的自动化用例相关的执行入口'''
# import time
# import unittest
# from HTMLTestRunner import HTMLTestRunner
# from ApiTestCase.testcase import Test
#
# t = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
# # 创建一个测试套件testcases
# testcases = unittest.TestSuite()
# # 往测试套件添加测试用例
# testcases.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))
#
# # 定义测试报告生成的路径：
# report_dir = './report/{}.html'.format(t)
# # 往测试报告写入测试结果，w表示打开文件的方式是“写入”,b表示二进制
# file = open(report_dir, 'wb')
#
# # 通过HTMLTestRunner运行测试套件
# runner = HTMLTestRunner(
#     title="xx商城项目",
#     description="自动化用例测试报告",
#     stream=file,
#     verbosity=2,
# )
# runner.run(testcases)

'''pytest方式运行所有的接口自动化用例
执行所有的接口用例，改一下pytest.ini文件
'''
import pytest
pytest.main(['--html=./report/test.html'])


