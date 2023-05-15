import pytest


def test01():
    print('测试用例01')


def test02():
    print('测试用例02')


def test03():
    print('测试用例03')


class Testcase():
    def setup_class(self):
        print("-----1-->setup_class")

    def teardown_class(self):
        print("----2--->teardown_class")
    def setup(self):
        print("------->setup_method")

    def teardown(self):
        print("------->teardown_method")
    def test04(self):
        # assert False
        print('测试类里面的---测试用例01')

    def test05(self):
        print('测试类里面的---测试用例02')

    def test06(self):
        print('测试类里面的---测试用例03')


if __name__ == "__main__":
    # pytest.main(['-s', 'test.py','--html=./test05.html'])
    pytest.main([ 'test.py','-s', '--alluredir=./test'])
