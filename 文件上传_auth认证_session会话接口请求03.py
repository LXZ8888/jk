import requests
import base64
'''第一个接口;文件上传:参数 files
f=[(key,value)]
'''
# url_file='http://127.0.0.1:7001/api/qingfeng/upload'
# f=[
#     #key        value
#     ('myfile',open(r'C:\Users\admin\Desktop\11111.png','rb')), #整体，代表上传一张图片
#     #('myfile', open(r'C:\Users\admin\Desktop\QQ截图20211108133957.png', 'rb')),
#
# ]
# res=requests.request(method='post',url=url_file,files=f)
# print(res.status_code)
# print(res.json())


'''第二个接口：auth认证'''
url_auth='http://127.0.0.1:7001/api/qingfeng/auth'
d={
    "id":123456789
}

user,pwd='admin','123456'  #把用户名和密码转化成YWRtaW46MTIzNDU2
users=base64.b64encode(bytes(user,encoding='utf-8')+b":"+
                       bytes(pwd,encoding='utf-8')).decode('ascii')
print(users)
h={
    #YWRtaW4xMTExOjEyMzQ1NjIy
    "Authorization":"Basic {}".format(users)
    #"Authorization": "#Bearer tyuyiuiuuuoiuooif"

}#请求头

res=requests.request(method='post',url=url_auth,json=d,headers=h)
print(res.status_code)
print(res.json())


'''session:跨请求保持某些参数'''
h={
    "Token":"qingfengtest",
    #"Authorization":"Basic {}".format(users)
}
url_users='http://127.0.0.1:7001/api/qingfeng/users'
url_one='http://127.0.0.1:7001/api/qingfeng/user/1'
'''通过requests模块里面的request方法，俩次请求完全独立'''
res1=requests.request(method='get',url=url_users,headers=h)
print(res1.status_code)
print(res1.json())
#
# res2=requests.request(method='get',url=url_one,headers=h)
# print(res2.status_code)
# print(res2.json())

'''通过session会话------统一添加请求头，token'''
s=requests.session()#定义一个session对象 s
s.headers.update(
    h
) #会话统一设置headers,update并不是把现有的header的替换掉，而是去新增字段。如果字段以存在，就替换
s.headers.update({"cookie":"cookietest"})
s.auth=('admin','123456')
res1=s.request(method='get',url=url_users,)
res2=s.request(method='get',url=url_one,)
res3=s.request(method='post',url=url_auth,json=d)

print(res1.request.headers)
print(res2.request.headers)
print(res3.request.headers)
# print(res1.status_code)
# print(res1.json())
# print(res2.status_code)
# print(res2.json())
print(res3.status_code)
print(res3.json())