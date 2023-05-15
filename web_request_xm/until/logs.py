'''打印日志类封装:控制台打印，输出到文件'''

import logging,time

'''
日志级别：
CRITICAL > ERROR > WARNING > INFO > DEBUG
debug : 打印全部的日志,详细的信息
info : 确认一切按预期运行，记录
warning : 还能按预期工作，可能会出现的问题(例如。磁盘空间低”),
error : 代码报错，软件没能执行一些功能
critical : 一个严重的错误,这表明程序本身可能无法继续运行
'''

class Handle_Logs():
    def __init__(self):
        '''定义日志器，formatter对象，时间，日志路径'''
        self.logger=logging.getLogger(name='qingfeng')
        self.logger.setLevel(level=logging.INFO)
        fmt_log = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
        self.log_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        self.formatter=logging.Formatter(fmt=fmt_log)
        self.logger_path=r'D:\1967668484\git_rc\jk_zdh\10qf_frame_code\qf_frame\logs'

    def stream_handel(self):
        '''控制台处理器'''
        stream_handel=logging.StreamHandler()
        stream_handel.setLevel(level=logging.INFO)
        stream_handel.setFormatter(fmt=self.formatter)
        self.logger.addHandler(hdlr=stream_handel)

    def file_handle(self):
        '''文件处理器'''
        file_handel = logging.FileHandler(filename='{0}\{1}.log'.format(self.logger_path,self.log_time))
        file_handel.setLevel(level=logging.INFO)
        file_handel.setFormatter(fmt=self.formatter)
        self.logger.addHandler(hdlr=file_handel)


    def get_log(self):
        self.stream_handel()
        self.file_handle()
        return self.logger

logger=Handle_Logs().get_log()
if __name__ == '__main__':
    logger.info('tetetsadgas')

