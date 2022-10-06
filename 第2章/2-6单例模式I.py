"""
  -*- ecoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/06 12:47
  @Email: 2665109868@qq.com
  @function 单例的应用：数据库应用程序
"""
import sqlite3


class MetaSingleton(type):
    _instance = {}

    # 通过__call__方法通过元类创建单例
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print("Database Object DB1: ", db1)
print("Database Object DB2: ", db2)
