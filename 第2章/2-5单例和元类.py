"""
  -*- ecoding: utf-8 -*-
  @Author: zhaojingtong
  @Time  : 2022/10/06 9:06
  @Email: 2665109868@qq.com
  @function 元类是一个类的类，意味着该类式它的元类的实例
"""


# class MyInt(type):
#     def __call__(cls, *args, **kwargs):
#         print("***** Here's My int ****", args)
#         print("Now do whatever you want with these objects...")
#         return type.__call__(cls, *args, **kwargs)
#
#
# class int(metaclass=MyInt):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# i = int(4, 5)
class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)
