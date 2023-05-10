'''reeuqes进行post 类型的请求
#接口地址：https://www.showdoc.com.cn/1748987824134871/8149023188013644  密码123456  运行run.dy文件
post：
    请求数据类型为form表单，或者text文件，通过data传参
    请求数据类型为json类型，通过json传参
request.body请求参数
'''
import json

import requests









'''-----------通过data传参,请求数据类型为form表单--------------------'''
d={
    "userid":1,
} #参数定义成一个字典

url_form_data='http://127.0.0.1:7001/api/qingfeng/formdata'
res=requests.request(method='post',url=url_form_data,data=d)
print('res.request.body',res.request.body)

print(res.status_code)
print(res.json())

'''第二个接口-----------通过data传参,请求数据类型为text文件--------------------'''
# url_text='http://127.0.0.1:7001/api/qingfeng/text'
# d='qingfengtest'
# res=requests.request(method='post',url=url_text,data=d)
# print('res.request.body',res.request.body)
# print(res.status_code)
# print(res.json())


'''第三个接口-----------通过json传参--------------------'''
# url_json='http://127.0.0.1:7001/api/qingfeng/user'
# d={
#     "username":"qingfeng",
#     "phone":123455667
# } #字典
# res=requests.request(method='post',url=url_json,json=d)
# print(res.json())
# print('res.request.body',res.request.body)
# print(res.status_code)



'''第四个接口:json-----------通过data传参,特例：指定请求数据类型为JSON--------------------'''

url_json='http://127.0.0.1:7001/api/qingfeng/user'
d={
    "username":"qingfeng",
    "phone":123455667
} #字典
h={
    "content-type":"application/json"
} #字典
# #字典转化json
# d=json.dumps(d)
# res=requests.request(method='post',url=url_json,data=d,headers=h) #res响应体
# print('请求头信息headers',res.request.headers)
# print('请求的参数res.request.body',res.request.body)
# print(res.status_code)
# print('响应头信息headers',res.headers)
# print(res.json())
#

'''delete类型'''
# s=requests.session() #创建会话
# url_delete='http://127.0.0.1:7001/api/qingfeng/user/1'
# res=s.request(method='delete',url=url_delete)
# print(res.status_code)
# print(res.json())