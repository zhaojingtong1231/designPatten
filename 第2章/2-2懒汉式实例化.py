# -*- ecoding: utf-8 -*-
# @Author: zhaojingtong
# @Time  : 2022/10/05 10:26
# @Email: 2665109868@qq.com
# @function 懒汉式实例化能够确保在实际需要时才创建对象
#           懒汉式实例化是一种节约资源并仅在需要时才创建它们的方式


class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('__init__ method called ..')
        else:
            print('Instance already created:', self.getInstance())

    # 类方法让类模板具有记忆力
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()
print("object created", Singleton.getInstance())
s1 = Singleton()
