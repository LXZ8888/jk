import json
import requests
from until.RW_excel import *
from until.tool import *
class HttpRequest():
    def __init__(self):
        '''所有用例的前置操作：创建一个会话，统一设置headers参数'''
        self.s = requests.session()
        self.s.auth = ('admin', '123456')
        self.contType={
                "Token": "qingfengtest",
                'Content-Type':"application/json",}
        self.init_headers(self.contType)
    def init_headers(self,h):
        self.s.headers.update(h)

    def json_dict(self,args):
        '''json字符串和字典的转化
        为了处理excel表格读取数据的格式处理'''
        if args:
            args=eval(args)
            return args

    def args_loads(self,args):
        '''替换参数里面的公共变量，{{}}
        {"limit":1,"test":"{{token}}"}
        token}}
        :return :返回替换之后的参数
        '''
        for key,value in args.items():
            if isinstance(value,str): #判断数据是否是xx的类型（参数，参数类型）
                if value.startswith('{{') and  value.endswith('}}'):
                     name=value.split('{{')[1].split('}}')[0] #token
                     args[key]=read_bl(name)
        return args


    def duanyan(self,yuqi,shiji):
        '''断言：需要一个结果，一个返回值
        True:代表断言成功
        False：代表断言失败
        contains_string:token   str
        json_value_check:{"code":200}  str
        {'code': 200, 'data': [{'gender': 'boy', 'id': 1, 'name': '张三', 'phone': '15908767383'}]}
        '''
        #print(type(yuqi),yuqi)
        if "{" in yuqi and "}" in yuqi:
            yuqi = self.json_dict(yuqi)  # 从excel读取的字典默认是字符串,调用json_dict转化成字典
            res = json_value_check(yuqi, shiji)
        else:
            res=contains_string(yuqi,shiji)
        return res


    def sendRequest(self,url_path,method,args,v,rheaders=None,tiqu=None):
        '''支持post接口测试：支持form表单类型/json类型
            支持get类型，params传参
            '''

        rheaders=self.json_dict(rheaders)  #excel获取默认是字符串，转化成字典
        rheaders=self.args_loads(rheaders) #替换请求头里面的变量
        self.init_headers(rheaders)
        args=self.json_dict(args)    #入参为python的字典类型， 刚好是get/formdata的类型
        args=self.args_loads(args)    #变量提取

        # 入参类型为json的时候，通过data提交数据，需要把入参转化为json字符串
        if rheaders and 'application/json' in rheaders.values():
            args=json.dumps(args)
            # 更改会话的请求头：'Content-Type': "application/x-www-form-urlencoded",
        if rheaders and 'application/x-www-form-urlencoded' in rheaders.values():

            self.init_headers({'Content-Type': "application/x-www-form-urlencoded"})
        res=self.s.request(url=url_path,method=method,
                           params=args,
                           data=args)
        #print('每个请求的body参数',res.request.body) #每个请求的body参数
        self.init_headers(self.contType)
        respone=res.json()
        '''以上代码的步骤都是接口请求拿到响应值，
        提取变量肯定是拿到响应值之后的事情'''
        if tiqu:
            print('开始提取变量{},值为{}'.format(tiqu,respone[tiqu]))
            tiqu_name=tiqu+'_tiqu' #变量的名称
            tiqu_value=respone[tiqu]
            #写到excel
            write_bl(tiqu_name,tiqu_value)

        '''断言方法：
        就是预期结果和实际结果的比较'''
        #print('响应值,',respone)
        result=self.duanyan(v,respone)
        return respone,result  #函数返回多个值的时候，默认是元祖吧