import json

import requests


class HttpRequest:
    def __init__(self):
        '''所有用例的前置操作：创建一个会话，统一设置headers参数'''
        self.s = requests.session()
        self.s.auth = ('admin', '123456')
        self.s.headers.update({"Token": "qingfengtest",
                               'Content-Type': "application/json",
                               })

        '''JSON字符串和字典的转换'''

    def json_dict(self, args):
        if args:
            args = eval(args)

            # print(type(args), args)
            return args

    def sendRequest(self, url_path, method, args, rt=None):
        args = self.json_dict(args)  # 进行数据处理，调用上述方法

        if rt and rt =='json':
            args = json.dumps(args)  # 入参类型为json时，通过data提交数据，需要将入参转为json字符串
        # if rt and rt == 'formdata':
        #     self.in
        res = self.s.request(url=url_path, method=method, params=args, data=args)
        print(res.json())


        return res.json()
