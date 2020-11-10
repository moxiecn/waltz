import os
import sys
import time
import logging
from Singleton import SINGLETON


# 註釋聲明綁定本類到裝飾器類Singleton上.
@SINGLETON  # 如需打印不同路径的日志（运行日志、审计日志），则不能使用单例模式（注释或删除此行）。此外，还需设定参数name。
class Logger:
    def __init__(self,
                 set_level="INFO",
                 name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1],
                 log_name=time.strftime("%z_%Y-%m-%d.log", time.localtime()),
                 log_path=os.path.join(os.path.dirname(
                     os.path.abspath(__file__)), "log"),
                 use_console=True):
        """
        :param set_level: 日志级别["NOTSET"|"DEBUG"|"INFO"|"WARNING"|"ERROR"|"CRITICAL"]，默认为INFO
        :param name: 日志中打印的name，默认为运行程序的name
        :param log_name: 日志文件的名字，默认为当前时间（年-月-日.log）
        :param log_path: 日志文件夹的路径，默认为alog.py同级目录中的log文件夹
        :param use_console: 是否在控制台打印，默认为True
        """
        if not set_level:
            set_level = self._exec_type()  # 设置set_level为None，自动获取当前运行模式
        self.__logger = logging.getLogger(name)  # 從logging模塊中得到的一個logger實例
        self.setLevel(
            getattr(logging, set_level.upper()) if hasattr(logging, set_level.upper()) else logging.INFO)  # 设置日志级别
        if not os.path.exists(log_path):  # 创建日志目录
            os.makedirs(log_path)
        formatter = logging.Formatter(
            "%(asctime)s - [%(lineno)d.%(levelno)s.%(levelname)s.%(name)s] - %(filename)s.%(funcName)s - %(message)s")  # 設置日誌格式器
        handler_list = list()  # 聲明一個處理器list對象
        handler_list.append(
            logging.FileHandler(os.path.join(log_path, log_name), encoding="utf-8"))  # list中放一個文件型日誌處理器以utf8編碼
        if use_console:  # 如果入參指定輸出至屏幕再將list中放入一個stream日誌處理器
            handler_list.append(logging.StreamHandler())

        for handler in handler_list:  # 將以上放在list中的處理器統一格式化
            handler.setFormatter(formatter)
            self.addHandler(handler)

    def __getattr__(self, item):
        return getattr(self.logger, item)

    @property
    def logger(self):
        return self.__logger

    @logger.setter
    def logger(self, func):
        self.__logger = func

    def _exec_type(self):
        return "DEBUG" if os.environ.get("IPYTHONENABLE") else "INFO"
