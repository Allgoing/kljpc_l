import configparser
import threading
import os


class Config:
    # __new__ 用于创建实例，而__init__用于初始化实例
    __configfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    __flag = False
    __instance_lock = threading.Lock() # 定义一把锁

    def __init__(self):
        # 如果配置初始化已经完成，直接返回
        if Config.__flag:
            return

        config = configparser.ConfigParser()
        config.read(Config.__configfile, encoding='UTF-8')
        self.__testcasefile = config.get('TestCaseFile', 'file')
        self.__logpath = config.get('LogPath', 'path')
        self.__database = config.get('DataBase', 'SQLALCHEMY_DATABASE_URI')
        Config.__flag = True

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls.__instance_lock.acquire()
            if not hasattr(cls, '_instance'):
                cls._instance = super().__new__(cls)
            cls.__instance_lock.release()

        return cls._instance


    @property
    def testCaseFile(self):
        return self.__testcasefile

    @property
    def logPath(self):
        return self.__logpath

    @property
    def database(self):
        return self.__database
