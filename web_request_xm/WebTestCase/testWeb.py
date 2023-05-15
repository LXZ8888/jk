'''xx1模块的web自动化用例：
都是需要登录的
'''

from PO.loginpage import LoginPage
from PO.homepage import HomePage

class TestCase01(HomePage):
    '''
    TestCase是用例类
    '''
    def test_search01(self,browser_login):
        '''搜索的用例:
        browserInit:一个已经登录过的浏览器对象，
        '''
        print('web自动化用例01')
        #browserInit==browser
        self.search(browser_login,'包包')





