# -*- coding: gbk -*-
print('����Ŀ��Ŀ¼�µ�conftest�ļ�')
import pytest
@pytest.fixture()
def openbrowser():
    print('�������')

@pytest.fixture()
def login():
    print('��¼')
    a=3
    return a