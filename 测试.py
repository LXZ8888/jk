import time

import requests
import unittest
from ddt import ddt, data, unpack
from HTMLTestRunner import HTMLTestRunner

new_topics = {
    "accesstoken": "5684eba8-f0df-41ec-b46c-d1f5351d153c",
    "title": "postman新增的帖子关联测试",
    "tab": "share",
    "content": "postman新增的帖子关联417"
}
def test03():
    url_text = 'http://81.71.38.70:3000/api/v1' + '/topics'
    res =requests.request(method='post', url=url_text, json=new_topics)
    print('新建主题', res)

test03()
