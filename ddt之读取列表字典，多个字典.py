import unittest
from ddt import ddt, data, unpack, file_data


# 导入ddt中的ddt,data,unpack方法


@ddt  # 首先用ddt装饰类
class caseddt_D2(unittest.TestCase):

    # 单个列表字典，未拆分

    @data([{"name": "peter", "age": 15, "addr": "chengdu"}])
    def test_8(self, value):
        print('单个列表字典，未拆分')
        print(value)

    # 多个列表字典，拆分
    @data([{"name": "peter", "age": 16, "addr": "chengdu"}, {"name": "lily", "age": 17, "addr": "chengdu"}])
    @unpack
    # 使用unpack拆分，列表或元组中几个参数就要在方法中传几个参数，列表中的字典看成一个整体，代表一个参数
    def test_9(self, value1, value2):
        print('多个列表字典，拆分')
        print(value1, value2)

    # 单个字典，拆分
    # @data里的数据key必须与方法里的key保持一致
    @data({"name": "jack", "age": 20})
    @unpack
    def test_10(self, name, age):
        print(name, age)

    # 多个字典, 拆分
    @data({"name": "peter", "age": 18, "addr": "chengdu"}, {"name": "lily", "age": 19, "addr": "chengdu"})
    @unpack
    def test_11(self, name, age, addr):
        print('多个字典, 拆分')
        print(name, age, addr)

    # 多个列表字典，用unpack拆分，多个参数时，要传多个参数，不能分别读取数据，*号拆分去掉最外层的括号，可以分别读取数据
    testdata = [{"name": "peter", "age": 21, "addr": "chengdu"}, {"name": "lily", "age": 22, "addr": "chengdu"}]

    @data(testdata)
    @unpack
    def test_12(self, value1, value2):
        print('多个列表字典，引用数据')

        print(value1, value2)

    # @data(*testdata)：*号意为解包，ddt会按逗号分隔，将数据拆分，可以分别读取数据（@unpack不能分别读取数据），*号只能去掉最外面一层括号

    testdata_A = [{"name": "peter", "age": 23, "addr": "chengdu"}, {"name": "lily", "age": 24, "addr": "chengdu"}]

    @data(*testdata_A)
    def test_13(self, value):
        print('1*号意为解包')
        print(value)


if __name__ == '__main__':
    unittest.main(verbosity=2)
