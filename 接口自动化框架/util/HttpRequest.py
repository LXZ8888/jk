import json

import requests
from util.RW_excel import ExcelWR
E = ExcelWR(filePath=r'../config/jk-sj.xlsx')  # 路径
# caseDatas = E.readEx()



class HttpRequest:
    def __init__(self):
        '''所有用例的前置操作：创建一个会话，统一设置headers参数'''
        self.s = requests.session()
        self.s.auth = ('admin', '123456')
        self.contType = {
            "Token": "qingfengtest",
            'Content-Type': "application/json", }
        self.init_headers(self.contType)

        '''JSON字符串和字典的转换'''

    def init_headers(self, h):
        self.s.headers.update(h)

    def json_dict(self, args):
        if args:
            args = eval(args)

            # print(type(args), args)
            return args

        # 替换参数里面的公共变量{{}}    return :返回替换之后的参数
    def args_loads(self,args):
        for key,value in args.items():
            if isinstance(value,str):
                if value.startswith('{{') and value.endswith('}}'):
                    name = value.split('{{')[1].split('}}')[0]
                    args[key] = E.read_tiqu(name)  # 读取excel变量,实例变量
        return args


    def sendRequest(self, url_path, method, args, rt=None,tiqu=None):
        args = self.json_dict(args)  # 进行数据处理，调用上述方法
        args=self.args_loads(args)


        if rt and rt =='json':
            args = json.dumps(args)  # 入参类型为json时，通过data提交数据，需要将入参转为json字符串
        if rt and rt == 'formdata':
            self.init_headers({'Content-Type': "application/x-www-form-urlencoded"})
        res = self.s.request(url=url_path, method=method, params=args, data=args)
        print(res.request.body) #打印每个post
        self.init_headers(self.contType)
        response=res.json()
        if tiqu:
            print('开始提取变{},值为{}'.format(tiqu,response[tiqu]))
            tiqu_name=tiqu+'_tiqu'  #变量的名称
            tiqu_value=response[tiqu]
            #写入excel表格
            E.write_tiqu(tiqu_name, tiqu_value)
        return res.json()
