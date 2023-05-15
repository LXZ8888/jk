'''封装一些公共的方法'''

def contains_string(yuqi,shiji):
    '''
    函数实现的功能：判断一个字典是否包含一个字符串
    :param yuqi:
    :param shiji:
    :return:
    '''
    if isinstance(yuqi, int):
        yuqi = str(yuqi)
    for key, value in shiji.items():
        # 1.预期是字符串，实际结果的value是字符串
        if isinstance(value, str):
            if yuqi in key or yuqi in value:
                return True
        # 2.预期是字符串，实际结果的value是整数
        if isinstance(value, int):
            value = str(value)
            if yuqi in key or yuqi in value:
                return True
        # 3.预期是字符串，实际结果的value是字典
        # 判断一个字典是否包含字符串
        if isinstance(value, dict):
            # for key1,value1 in value.items():
            if yuqi in key :
                return True
            #判断预期是否在value里面
            res = contains_string(yuqi, value)
            if res is True:
                return True
        # 4.预期是字符串，实际结果的value是列表
        if isinstance(value, list):
            for l in value:
                # l又变成字典，
                if yuqi in key:
                    return True
                res = contains_string(yuqi, l)
                if res is True:
                    return True
    # 循环结束，如果函数还没有结束，没有任何一种情况返回为真，说明断言失败，False
    return False

# yuqi = {"httpstatus": 200,"msg":"success",
#         "info":{"name":"admin"},
#         "data":[1,{"id":1}]} #这个列表第几个字典（索引），哪个字段的值
# shiji = {
#         "adress": {
#             "city": "changsha",
#         },
#         "httpstatus": 200,
#         "info": {
#             "age": 18,
#             "name": "admin",
#             "test1":"ttttt"
#         },
#         "msg": "success",
#         "token": "qingfengtest",
#         "data":[
#             {
#                 "id1":'id1',
#                 "phone1":"phone1"
#             },
#             {
#                 "id2":'id2',
#                 "phone2": "phone2",
#
#             },
#             {
#                 "id3":'id3',
#                 "phone3": "phone3"
#
#             }
#     ]
#     }

yuqi={"data":[1,{"id":1}]}
shiji={'code': 200, 'data': [
    {'gender': 'boy', 'id': 1, 'name': '张三', 'phone': '15908767383'},
    {'gender': 'boy', 'id': 2, 'name': '张三', 'phone': '15908767383'}]}
def json_value_check(yuqi,shiji):
    '''
    判断一个字典是否包含一个字典(支持多个key的校验)
    :param yuqi:
    :param shiji:
    :return:
    1.循环yuqi这个字典？只需要验证预期结果里面的 该字段
    '''

    for key,value in yuqi.items():
        if key not in shiji:
            #如果不加这层的判断，代码报错
            return False
        else:
            #因为实际结果的value,可能是字符串（整数），可能是列表，可能是字典
            #key=msg,value,success
            #1.预期结果key是字符串，实际结果的key也是字符串
            if isinstance(shiji[key],str) or isinstance(shiji[key],int):
                #key=httpstatus,
                #value=200
                if value!=shiji[key]:
                    #想要支持多个的校验，想要预期结果一直循环下去，校验,
                    #直到有校验不通过的，才返回false
                    #return True
                    return False
            #2.预期结果key字典，实际结果的key是字典
            if isinstance(value,dict) or isinstance(shiji[key],dict):
                    #"info":{"name":"admin"}
                    res=json_value_check(value,shiji[key])
                    if res is False:
                        return False
            #3.预期结果key列表，实际结果的key是列表
            if isinstance(value,list) or isinstance(shiji[key],list):
                    # print(value)
                    # print(value[0],len(shiji[key]))
                    # #实际长度为3，用户最多填个3
                    if value[0]>len(shiji[key]):
                        return False
                    else:
                        res=json_value_check(value[1],shiji[key][value[0]-1]) #shiji['data'][0]
                        if res is False:
                            return False
    #循环结束，如果函数还没有return结束，没有任何一种情况返回为假，说明断言成功
    return True

if __name__ == '__main__':
    #print(contains_string(yuqi,shiji))
    print(json_value_check(yuqi,shiji))