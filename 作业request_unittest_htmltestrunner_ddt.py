import json
import time

import requests
import unittest
from ddt import ddt, data, unpack
from HTMLTestRunner import HTMLTestRunner
from ddt import ddt, data, unpack

# users=[
#     ('admin','123456'),
#     ('admin','123456xxx'),
#     ('adminxxx', '123456xxx'),
# ]
new_token = '7ca7865a-81ca-4008-ada7-85bec7898a4f'
new_topic_id = "645a1e90761b999432e758b1"

'''新建主题'''
new_topics = [
    {
        "accesstoken": new_token,
        "title": "python新增嘿嘿嘿1",
        "tab": "share",
        "content": "postman新增的帖子关联417"
    },
    {
        "accesstoken": new_token,
        "title": "python新增好好玩我哈哈哈2",
        "tab": "share",
        "content": "postman新增的帖子关联417"
    }
]
'''编辑主题'''
edit_topic = {
    "accesstoken": new_token,
    "topic_id": new_topic_id,
    "title": "postman修改的帖子501",
    "tab": "share",
    "content": "postman修改的帖子417"
}
'''收藏主题'''
collect_topic = {
    "accesstoken": new_token,
    "topic_id": new_topic_id
}
'''取消主题'''
cancelTopic = {
    "accesstoken": new_token,
    "topic_id": new_topic_id
}
''' 新建评论'''
new_reply = {
    "accesstoken": new_token,
    "content": "python新建评论5"
}

'''为评论点赞'''
likeReply = {
    "accesstoken": new_token
}
'''验证 accessToken 的正确性'''
confirmToken = {
    "accesstoken": new_token
}
''' 获取未读消息数'''
unread = {
    "accesstoken": new_token
}
'''获取已读和未读消息'''
read = {
    "accesstoken": new_token
}
'''标记全部已读'''
read_ok = {
    "accesstoken": new_token
}
''' 标记单个消息为已读'''
onlyRead = {
    "accesstoken": new_token
}


@ddt
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.s = requests.session()
        # self.s.headers.update({"accesstoken": "5684eba8-f0df-41ec-b46c-d1f5351d153c"})
        self.urlBase = 'http://81.71.38.70:3000/api/v1'

    '''-----------------主题首页-------------------------'''

    def test01(self):
        url_text = self.urlBase + '/topics'
        res = self.s.request(method='get', url=url_text)
        print(res.json())
        '''断言'''
        self.assertEqual(res.status_code, 200)

    '''-----------------主题详情-------------------------'''

    def test02(self):
        url_text = self.urlBase + '/topic/6459ec87761b999432e7588d'
        res = self.s.request(method='get', url=url_text)
        print(res.json())

    '''----------------- 新建主题-------------------------'''

    ''' "accesstoken": new_token,
        "title": "python新增的帖子关联hhh1",
        "tab": "share",
        "content": "postman新增的帖子关联417"'''

    @data(*new_topics)
    # @unpack
    def test03(self, value):
        print('new_topics', new_topics)
        print('dayu',value)
        url_text = self.urlBase + '/topics'
        res = self.s.request(method='post', url=url_text, json=value)
        print('新建主题', res)
        print('新建主题body', res.request.body)

    '''编辑主题'''

    def test04(self):
        url_text = self.urlBase + '/topics/update'
        res = self.s.request(method='post', url=url_text, json=edit_topic)
        print('编辑主题', res.request.body)
        '''断言'''

    # '''断言'''
    # self.assertEqual(res.status_code, 200)
    '''收藏主题'''

    def test05(self):
        url_text = self.urlBase + '/topic_collect/collect'
        res = self.s.request(method='post', url=url_text, json=collect_topic)
        print('收藏主题', res)
        '''断言'''
        self.assertEqual(res.status_code, 200)

    # '''断言'''
    # self.assertEqual(res.status_code, 200)

    '''取消主题'''

    # def test06(self):
    #     url_text = self.urlBase + '/topic_collect/de_collect '
    #     res = self.s.request(method='post', url=url_text, json=cancelTopic)
    #     print('取消主题', res)

    # '''断言'''
    # self.assertEqual(res.status_code, 200)
    '''用户所收藏的主题'''

    def test07(self):
        url_text = self.urlBase + '/topic_collect/qingfeng01'
        res = self.s.request(method='get', url=url_text)
        print('用户所收藏的主题', res)
        '''断言'''
        self.assertEqual(res.status_code, 200)

    '''新建评论'''

    def test08(self):
        url_text = self.urlBase + '/topic/6459d896761b999432e7586b/replies'
        res = self.s.request(method='post', url=url_text, json=new_reply)
        print('新建评论', res)
        '''断言'''
        self.assertEqual(res.status_code, 200)

        ''' 为评论点赞'''

    def test09(self):
        url_text = self.urlBase + '/reply/645a24ad761b999432e758cc/ups'
        res = self.s.request(method='post', url=url_text, json=likeReply)
        print(' 为评论点赞', res)
        print(' 为评论点赞', res.request.body)
        '''断言'''
        self.assertEqual(res.status_code, 200)

        '''用户详情'''

    def test010(self):
        url_text = self.urlBase + '/user/qingfeng01'
        res = self.s.request(method='get', url=url_text)
        print('用户详情', res)
        '''断言'''
        self.assertEqual(res.status_code, 200)

    '''验证 accessToken 的正确性'''

    def test011(self):
        url_text = self.urlBase + '/accesstoken'
        res = self.s.request(method='post', url=url_text, json=confirmToken)
        print('验证 accessToken 的正确性', res)
        self.assertEqual(res.status_code, 200)

    def test012(self):
        url_text = self.urlBase + '/message/count'
        res = self.s.request(method='get', url=url_text, json=unread)
        print('获取未读消息数', res.json())

    def test013(self):
        url_text = self.urlBase + '/messages'
        res = self.s.request(method='get', url=url_text, json=read)
        print('获取已读和未读消息', res.json())

    def test014(self):
        url_text = self.urlBase + '/message/mark_all'
        res = self.s.request(method='post', url=url_text, json=read_ok)
        print('标记全部已读', res)
        '''断言'''
        self.assertEqual(res.status_code, 200)
    #
    # def test015(self):
    #     url_text = self.urlBase + 'message/mark_one/6433a9b8761b999432e748de'
    #     res = self.s.request(method='post', url=url_text, json=onlyRead)
    #     print('标记单个消息为已读', res)


if __name__ == '__main__':
    # unittest.main()
    t = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    testcases = unittest.TestSuite()
    testcases.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))
    runner = unittest.TextTestRunner()
    report_dir = './test_report_{}.html'.format(t)
    file = open(report_dir, 'wb')
    # 通过HTMLTestRunner运行测试套件
    runner = HTMLTestRunner(
        title="论坛项目测试用例",
        description="自动化用例测试报告",
        stream=file,
        verbosity=2,
    )
    runner.run(testcases)
