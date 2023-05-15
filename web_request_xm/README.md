#xx公司自动化测试框架1.0

###环境搭建
	1.安装python3.8+版本
	2.安装python依赖包：pip install -r requirement.txt

###框架简介
	1.实现web/接口自动化，支持数据驱动
	2.基础架构python、selenium、POM模式、request，unittest，pytest，ddt

###使用说明
	接口自动化执行入口：python run  run_api.py
	web自动化执行入口：python run  run_web.py

###框架的目录结构说明
	report:存放测试报告
	config：基础数据存放，数据库账号，url前缀
    until：公共模块方法封装
    pytest.ini 配置文件
    README.md 文件说明
