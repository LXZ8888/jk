'''接口自动化测试：导入requests库
requests.request
requests.get
底层调用的都是同一个请求
接口地址：http://81.71.38.70:3000/api/v1/
'''

import requests,json
'''接口1：论坛项目 获取主题首页'''


'''写法3种request'''
#1.requests模块里面的request方法，发起http请求，2.接收http响应
#requests.request('请求方法','接口地址')
#res1=requests.request('get','http://1.13.5.210:3000/api/v1/topics')
#res2=requests.request(url='http://1.13.5.210:3000/api/v1/topics',method='get')



'''get类参数1.直接拼接在url    2.通过params传参'''
# res1=requests.request('get','http://81.71.38.70:3000/api/v1/topics?limit=1')  #传参方式一   返回值是一个字典，为了便于阅读，格式化处理

# p={
#     "limit":1,
#     "tab":"share"
# } #参数定义成一个字典
#
# def test(**kwargs):
#     print(kwargs)
# test(params=p,test=1)
# res1=requests.request('get', 'http://1.13.5.210:3000/api/v1/topics',params=p)

'''请求携带参数:cookie、token'''
'''接口3:12306'''
h={
    "Cookie":"_uab_collina=163171289127393441288275; JSESSIONID=A480B7E51DB427E671A9EAB429E0BF57; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u957F%u6C99%2CCSQ; BIGipServerotn=1173357066.50210.0000; BIGipServerpool_passport=233046538.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; RAIL_EXPIRATION=1643100119736; RAIL_DEVICEID=sNfoLXTkSZyQ1Tk8feRzN3lS3MxlI5FBh2gCXgv5KRsU_DY4muckz0RS4M3FSq0NQVgclu6vPWcf_iS5q99UOyf58Px-VxHptormzrtjDPtelGTqyEtNunOscPbFFI6Zgs2IqJsx_X3JEaQ-z7RfDQ-T78O2LGDb; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_toDate=2022-01-22; _jc_save_fromDate=2022-01-25"
}

res=requests.get(url='https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2022-01-25&leftTicketDTO.'
                     'from_station=SHH&leftTicketDTO.to_station=CSQ&purpose_codes=ADULT',
                 headers=h)

# print(res.text)
# print(res.content)
print(res.json())  #确定返回值是JSON格式

'''接口2：请求多个参数。获取用户信息'''
# h={"token":"qingfengtest"} #定义的一个请求头，字典类型
# p={"limit":1}#定义的参数，字典类型
# res=requests.request(method='get',
#                      url='http://127.0.0.1:7001/api/qingfeng/users',
#                      params=p,
#                      headers=h)
#
# print(res.status_code)
# print(res.json())



'''3.响应体res1（状态码，响应值，响应头信息）'''
#print('状态码',res1.status_code) #状态码
# print('响应值',type(res1.text),res1.text,)         #响应值,text方法获得的是字符串
# print('响应值',type(res1.content),res1.content)    #响应值，bytes字节类型
#print('响应值',type(res1.json()),res1.json())      #响应值，获取的是字典类型

#respone=res1.json() #响应值respone,字典类型
#print(respone)  #打印字典类型的响应值
#print(json.dumps(respone,indent=4,ensure_ascii=False)) #等于把显示在一行的字典，放bejson格式化校验
# respone=res1.json() #响应值respone,字典类型
# print('转化之前',type(respone))
# respone=json.dumps(respone) #把respone字典转化为json字符串
# print('转化之后',type(respone))

# respone=json.loads(respone) #把json字符串转化为字典
# print('转化之后',type(respone))


'''python字典和 json字符串直接的相互转化'''

#print('响应头信息',res1.headers)     #响应头信息：接口返回给前端的头信息（返回的数据类型）

# print(res2)





