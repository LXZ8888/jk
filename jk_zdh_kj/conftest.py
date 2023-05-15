# -*- coding: gbk -*-
print('本项目根目录下的conftest文件')
import pytest
@pytest.fixture()
def openbrowser():
    print('打开浏览器')

@pytest.fixture()
def login():
    print('登录')
    a=3
    return a