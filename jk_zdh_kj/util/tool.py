'''封装一些公共的方法
断言方法
'''

'''
yuqi = {"httpstatus": 200,"msg":"success",
        "info":{"name":"admin"},
        "data":[1,{"id":1}]} #这个列表第几个字典（索引），哪个字段的值
shiji = {
        "adress": {
            "city": "changsha",
        },
        "httpstatus": 200,
        "info": {
            "age": 18,
            "name": "admin",
            "test1":"ttttt"
        },
        "msg": "success",
        "token": "qingfengtest",
        "data":[
            {
                "id1":'id1',
                "phone1":"phone1"
            },
            {
                "id2":'id2',
                "phone2": "phone2",

            },
            {
                "id3":'id3',
                "phone3": "phone3"

            }
    ]

'''

def contains_string(yuqi,shiji):
    '''
    #判断一个字典是否包含一个字符串
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

'''yuqi'''

def json_value_check(yuqi,shiji):
    for key, value in yuqi.items():
        if key not in shiji:
            return False
        else:
            # 因为实际结果的value,可能是1字符串（整数），2可能是列表，3可能是字典
            # 1.预期结果key是字符串，实际结果的key也是字符串
            if isinstance(shiji[key], str) or isinstance(shiji[key], int):
                if value != shiji[key]:
                    return False
            # 2.预期结果key字典，实际结果的key是字典
            if isinstance(value, dict) or isinstance(shiji[key], dict):
                # "info":{"name":"admin"}
                res = json_value_check(value, shiji[key])
                if res is False:
                    return False
            # 3.预期结果key列表，实际结果的key是列表
            if isinstance(value, list) or isinstance(shiji[key], list):
                if value[0] > len(shiji[key]):
                    return False
                else:
                    res = json_value_check(value[1], shiji[key][value[0] - 1])
                    if res is False:
                        return False

    return True

if __name__ == '__main__':
    yuqi = 'dqi'
    shiji = {
        "adress": {
            "city": "changsha",
        },
        "httpstatus": 200,
        "info": {
            "age": 18,
            "name": "admin"
        },
        "msg": "success",
        "token": "qingfengtest",
        "data":[
            {
                "idqingfeng":'id1'
            },
            {
                "id":'id2'
             }
    ]
    }

    print(contains_string(yuqi,shiji))